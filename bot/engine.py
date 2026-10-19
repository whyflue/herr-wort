"""Машина состояний бота: меню, сюжет, тренировка, отработка ошибок.

Движок не знает про VK: он принимает текст сообщения и возвращает список
действий вида {"edit": bool, "text": ..., "keyboard": ...}, которые транспорт
(main.py или simulate.py) превращает в сообщения. Так сценарий можно
прогонять в консоли без токена и без риска для аккаунта.
"""

import logging

import content
from bot import render, texts

log = logging.getLogger(__name__)


def send(text: str, keyboard: dict = None, edit: bool = False) -> dict:
    return {"edit": edit, "text": text, "keyboard": keyboard}


class Engine:
    def __init__(self, db):
        self.db = db

    # ---------- точка входа ----------

    def handle(self, vk_id: int, text: str) -> list:
        state = self.db.get_state(vk_id)
        state.setdefault("phase", "menu")
        try:
            actions = self._dispatch(vk_id, state, text or "")
        except Exception:  # pragma: no cover - защита от неожиданных состояний
            log.exception("Сбой в диалоге с %s", vk_id)
            state = {"phase": "menu"}
            actions = [
                send("⚙️ Что-то заело в струнах. Бард начинает заново.\n"
                     "Если ошибка повторится — сообщите автору бота."),
                *self._menu(vk_id, state, greeting=False),
            ]
        self.db.set_state(vk_id, {k: v for k, v in state.items() if k != "_tmp"})
        return actions

    def _dispatch(self, vk_id: int, st: dict, text: str) -> list:
        command = texts.resolve(text)
        phase = st.get("phase", "menu")

        # Общие команды — работают с любого экрана.
        if command in ("start", "menu"):
            return self._menu(vk_id, st, greeting=command == "start")
        if command == "help":
            st["phase"] = "help"
            return [send(*render.help_screen())]
        if command == "stats":
            st["phase"] = "stats"
            return [send(*self._stats(vk_id))]
        if command == "restart":
            st["phase"] = "restart_confirm"
            return [send(*render.restart_confirm())]
        if command == "restart_no":
            return self._menu(vk_id, st)
        if command == "restart_yes":
            self.db.reset_story(vk_id)
            st.clear()
            st["phase"] = "menu"
            return [
                send("🔄 Свиток порван, бард снова в Любеке. Историю ошибок "
                     "и статистику оставили — они пригодятся."),
                *self._menu(vk_id, st, greeting=False),
            ]

        handler = getattr(self, "_on_" + phase, None)
        result = None
        if handler is not None:
            result = handler(vk_id, st, text, command)
        if result is None:
            result = self._task_input(vk_id, st, text)
        if result is not None:
            return result

        # Ничего не подошло: подсказка и повтор текущего экрана.
        if not texts.normalize(text):
            # Пустое сообщение (стикер, фото) — просто показываем экран снова.
            return self._current(vk_id, st)
        return [send(*render.fallback()), *self._current(vk_id, st)]

    # ---------- экраны ----------

    def _menu(self, vk_id: int, st: dict, greeting: bool = False) -> list:
        done = self.db.done_topics(vk_id)
        complete = len(done) >= len(content.TOPICS)
        st["phase"] = "menu"
        text, keyboard = render.main_menu(len(done), bool(done), complete)
        actions = []
        if greeting:
            actions.append(send(
                "🎻 Привет, путник! Я бард: хожу по немецким городам, учусь "
                "говорить и складываю балладу. Пойдём со мной — подскажешь "
                "мне правила, а я спою.\n\nВыбери, куда идти:"
            ))
        if complete:
            actions.append(send("🏁 Баллада уже дописана. Можно вернуться "
                                "в знакомые места или начать путь заново."))
        actions.append(send(text, keyboard))
        return actions

    def _stats(self, vk_id: int) -> tuple:
        done = self.db.done_topics(vk_id)
        results = {topic["id"]: self.db.topic_results(vk_id, topic["id"])
                   for topic in content.TOPICS}
        return render.stats_screen(self.db.overall_stats(vk_id), done, results)

    def _current(self, vk_id: int, st: dict) -> list:
        """Повторяет текущий экран (для устаревших кнопок и непонятного ввода)."""
        phase = st.get("phase", "menu")
        if phase == "place":
            topic = content.get_topic(st["topic"])
            return [send(*render.place(topic, st.get("ctx", "story")))]
        if phase == "theory":
            topic = content.get_topic(st["topic"])
            return [send(*render.theory_page(topic, st.get("page", 0), st.get("ctx", "story")))]
        if phase == "task":
            return self._render_task(vk_id, st)
        if phase == "feedback":
            last = st.get("last")
            if last:
                topic = content.get_topic(st["topic"])
                exercise = content.find_exercise(topic, last["ex"])
                variant = content.variant(exercise, last.get("retry", 0))
                return [send(*render.feedback(variant, last["kind"], last["ok"],
                                              last["right"], bool(last.get("retry"))))]
        if phase == "retry_offer":
            topic = content.get_topic(st["topic"])
            return [send(*render.retry_offer(topic, st.get("wrong_ids") or []))]
        if phase == "song":
            topic = content.get_topic(st["topic"])
            done = self.db.done_topics(vk_id)
            return [send(*render.song(topic, len(done), len(done) >= len(content.TOPICS)))]
        if phase == "finale":
            return [send(*render.finale(self.db.done_topics(vk_id)))]
        if phase == "topic_list":
            return [send(*render.topic_list(self.db.done_topics(vk_id)))]
        if phase == "place_list":
            return [send(*render.place_list(self.db.done_topics(vk_id)))]
        if phase == "result":
            topic = content.get_topic(st["topic"])
            return [send(*render.result(topic, st.get("correct", 0),
                                        st.get("wrong", 0), st.get("ctx", "train")))]
        if phase == "restart_confirm":
            return [send(*render.restart_confirm())]
        if phase == "stats":
            return [send(*self._stats(vk_id))]
        if phase == "help":
            return [send(*render.help_screen())]
        return self._menu(vk_id, st)

    # ---------- меню: вход в режимы ----------

    def _on_menu(self, vk_id: int, st: dict, text: str, command: str):
        if command == "story":
            done = self.db.done_topics(vk_id)
            if len(done) >= len(content.TOPICS):
                st["phase"] = "finale"
                return [send(*render.finale(done))]
            topic_id = self._next_topic_id(done)
            actions = []
            if not done and not st.get("story_seen"):
                st["story_seen"] = 1
                actions.append(send(*render.story_intro()))
            actions.extend(self._select_topic(vk_id, st, topic_id, "story"))
            return actions
        if command == "train":
            return self._topic_list(vk_id, st)
        if command == "nostalgia":
            return self._place_list(vk_id, st)
        return None

    def _topic_list(self, vk_id: int, st: dict) -> list:
        st["phase"] = "topic_list"
        return [send(*render.topic_list(self.db.done_topics(vk_id)))]

    def _place_list(self, vk_id: int, st: dict) -> list:
        done = self.db.done_topics(vk_id)
        if not done:
            st["phase"] = "menu"
            return [
                send("🏰 Пока баллада не написана — и вспоминать нечего. "
                     "Начни с сюжета: бард ждёт в Любеке."),
                *self._menu(vk_id, st),
            ]
        st["phase"] = "place_list"
        return [send(*render.place_list(done))]

    def _next_topic_id(self, done: list) -> str:
        for topic in content.TOPICS:
            if topic["id"] not in done:
                return topic["id"]
        return content.TOPICS[-1]["id"]

    def _select_topic(self, vk_id: int, st: dict, topic_id: str, ctx: str) -> list:
        st["ctx"] = ctx
        st["topic"] = topic_id
        st["page"] = 0
        st["qi"] = 0
        st["queue"] = []
        st["build"] = []
        st["step"] = 1
        st["correct"] = 0
        st["wrong"] = 0
        st["wrong_ids"] = []
        st["retry_run"] = 0
        st["phase"] = "place"
        topic = content.get_topic(topic_id)
        return [send(*render.place(topic, ctx))]

    def _on_topic_list(self, vk_id: int, st: dict, text: str, command: str):
        if command == "to_topics":
            return self._topic_list(vk_id, st)
        topic_id = self._match_topic(text)
        if topic_id:
            return self._select_topic(vk_id, st, topic_id, "train")
        return None

    def _on_place_list(self, vk_id: int, st: dict, text: str, command: str):
        if command == "to_places":
            return self._place_list(vk_id, st)
        topic_id = self._match_topic(text)
        done = self.db.done_topics(vk_id)
        if topic_id and topic_id in done:
            return self._select_topic(vk_id, st, topic_id, "nostalgia")
        return None

    def _match_topic(self, text: str):
        norm = texts.normalize(text)
        if not norm:
            return None
        for topic in content.TOPICS:
            label = "{}. {}".format(topic["nr"], topic["short"])
            if norm in (texts.normalize(label), str(topic["nr"])):
                return topic["id"]
        return None

    # ---------- локация и теория ----------

    def _on_place(self, vk_id: int, st: dict, text: str, command: str):
        if command == "listen":
            return self._theory(vk_id, st, 0)
        if command == "to_tasks":
            return self._start_tasks(vk_id, st, retry=False)
        if command == "to_topics":
            return self._topic_list(vk_id, st)
        if command == "to_places":
            return self._place_list(vk_id, st)
        return None

    def _theory(self, vk_id: int, st: dict, page: int) -> list:
        topic = content.get_topic(st["topic"])
        page = max(0, min(page, len(topic["theory"]) - 1))
        st["page"] = page
        st["phase"] = "theory"
        return [send(*render.theory_page(topic, page, st.get("ctx", "story")))]

    def _on_theory(self, vk_id: int, st: dict, text: str, command: str):
        if command == "next":
            return self._theory(vk_id, st, st.get("page", 0) + 1)
        if command == "to_tasks":
            return self._start_tasks(vk_id, st, retry=False)
        return None

    # ---------- задания ----------

    def _start_tasks(self, vk_id: int, st: dict, retry: bool) -> list:
        topic = content.get_topic(st["topic"])
        if retry:
            known = {exercise["id"] for exercise in topic["exercises"]}
            ids = [ex_id for ex_id in (st.get("wrong_ids") or []) if ex_id in known]
            queue = [{"id": ex_id, "retry": 1} for ex_id in ids]
            st["wrong_ids"] = []
        else:
            queue = [{"id": exercise["id"], "retry": 0}
                     for exercise in topic["exercises"]]
        st["retry_run"] = 1 if retry else 0
        st["queue"] = queue
        st["qi"] = 0
        if not queue:
            return self._finish_run(vk_id, st)
        return self._render_task(vk_id, st)

    def _render_task(self, vk_id: int, st: dict, edit: bool = False) -> list:
        topic = content.get_topic(st["topic"])
        queue = st["queue"]
        index = min(st.get("qi", 0), len(queue) - 1)
        item = queue[index]
        exercise = content.find_exercise(topic, item["id"])
        variant = content.variant(exercise, bool(item.get("retry")))
        st["phase"] = "task"
        text, keyboard = render.task(
            topic, variant, index + 1, len(queue),
            build=st.get("build") or [],
            step=st.get("step", 1),
            is_retry=bool(item.get("retry")),
        )
        return [send(text, keyboard, edit=edit)]

    def _task_input(self, vk_id: int, st: dict, text: str):
        if st.get("phase") != "task" or not st.get("queue"):
            return None
        topic = content.get_topic(st["topic"])
        index = min(st.get("qi", 0), len(st["queue"]) - 1)
        item = st["queue"][index]
        exercise = content.find_exercise(topic, item["id"])
        variant = content.variant(exercise, bool(item.get("retry")))
        mechanics = content.kind_mechanics(variant["kind"])
        norm = texts.normalize(text)
        if not norm:
            return None

        if mechanics == "choice":
            labels = [texts.normalize(option) for option in variant["options"]]
            if norm not in labels:
                return None
            choice = labels.index(norm)
            ok = choice == variant["answer"]
            return self._answer(vk_id, st, topic, exercise, variant,
                                ok, variant["options"][variant["answer"]])

        if mechanics == "order":
            if norm == texts.normalize(texts.BTN_CHECK):
                build = st.get("build") or []
                if not build:
                    return self._render_task(vk_id, st)
                ok = texts.normalize(" ".join(build)) == texts.normalize(variant["answer"])
                return self._answer(vk_id, st, topic, exercise, variant,
                                    ok, variant["answer"])
            if norm == texts.normalize(texts.BTN_UNDO):
                build = st.get("build") or []
                if build:
                    build.pop()
                st["build"] = build
                return self._render_task(vk_id, st, edit=True)
            if norm == texts.normalize(texts.BTN_CLEAR):
                st["build"] = []
                return self._render_task(vk_id, st, edit=True)
            words = [texts.normalize(word) for word in variant["words"]]
            if norm in words:
                word = variant["words"][words.index(norm)]
                st["build"] = (st.get("build") or []) + [word]
                return self._render_task(vk_id, st, edit=True)
            return None

        # mechanics == "error"
        if st.get("step", 1) == 2 and variant.get("fix"):
            fix = variant["fix"]
            labels = [texts.normalize(option) for option in fix["options"]]
            if norm not in labels:
                return None
            choice = labels.index(norm)
            return self._answer(vk_id, st, topic, exercise, variant,
                                choice == fix["answer"], fix["options"][fix["answer"]])
        words = [texts.normalize(word) for word in variant["sentence"].split()]
        if norm not in words:
            return None
        ok = norm == texts.normalize(variant["wrong"])
        if ok and variant.get("fix"):
            st["step"] = 2
            st["phase"] = "task"
            return self._render_task(vk_id, st)
        right = variant["wrong"]
        if variant.get("fix"):
            fix = variant["fix"]
            right = "{} → {}".format(variant["wrong"], fix["options"][fix["answer"]])
        return self._answer(vk_id, st, topic, exercise, variant, ok, right)

    def _answer(self, vk_id: int, st: dict, topic: dict, exercise: dict,
                variant: dict, ok: bool, right: str) -> list:
        item = st["queue"][min(st.get("qi", 0), len(st["queue"]) - 1)]
        is_retry = bool(item.get("retry"))
        if ok:
            st["correct"] = st.get("correct", 0) + 1
            self.db.resolve_mistake(vk_id, exercise["id"])
        else:
            st["wrong"] = st.get("wrong", 0) + 1
            self.db.log_mistake(vk_id, topic["id"], exercise["id"])
            known = st.setdefault("wrong_ids", [])
            if exercise["id"] not in known:
                known.append(exercise["id"])
        st["phase"] = "feedback"
        st["step"] = 1
        st["build"] = []
        st["last"] = {
            "ex": exercise["id"],
            "kind": variant["kind"],
            "ok": ok,
            "right": right,
            "retry": 1 if is_retry else 0,
        }
        text, keyboard = render.feedback(variant, variant["kind"], ok, right, is_retry)
        return [send(text, keyboard)]

    def _on_feedback(self, vk_id: int, st: dict, text: str, command: str):
        if command != "next":
            return None
        st["qi"] = st.get("qi", 0) + 1
        if st["qi"] < len(st.get("queue") or []):
            return self._render_task(vk_id, st)
        return self._after_tasks(vk_id, st)

    # ---------- завершение темы ----------

    def _after_tasks(self, vk_id: int, st: dict) -> list:
        topic = content.get_topic(st["topic"])
        ctx = st.get("ctx", "story")
        if st.get("retry_run"):
            st["retry_run"] = 0
            return self._finish_run(vk_id, st)
        if ctx in ("story", "nostalgia") and st.get("wrong_ids"):
            st["phase"] = "retry_offer"
            return [send(*render.retry_offer(topic, st["wrong_ids"]))]
        return self._finish_run(vk_id, st)

    def _finish_run(self, vk_id: int, st: dict) -> list:
        topic = content.get_topic(st["topic"])
        ctx = st.get("ctx", "story")
        kind = {"story": "story", "train": "training", "nostalgia": "nostalgia"}
        self.db.save_attempt(vk_id, topic["id"], kind.get(ctx, "story"),
                             st.get("correct", 0), st.get("wrong", 0))
        if ctx == "story":
            self.db.mark_topic_done(vk_id, topic["id"])
            done = self.db.done_topics(vk_id)
            complete = len(done) >= len(content.TOPICS)
            st["phase"] = "song"
            return [send(*render.song(topic, len(done), complete))]
        st["phase"] = "result"
        return [send(*render.result(topic, st.get("correct", 0),
                                    st.get("wrong", 0), ctx))]

    def _on_retry_offer(self, vk_id: int, st: dict, text: str, command: str):
        if command == "retry_mistakes":
            return self._start_tasks(vk_id, st, retry=True)
        if command == "skip_retry":
            return self._finish_run(vk_id, st)
        return None

    def _on_result(self, vk_id: int, st: dict, text: str, command: str):
        if command == "retry_mistakes":
            return self._start_tasks(vk_id, st, retry=True)
        if command == "again":
            return self._select_topic(vk_id, st, st["topic"], st.get("ctx", "train"))
        if command == "to_topics":
            return self._topic_list(vk_id, st)
        if command == "to_places":
            return self._place_list(vk_id, st)
        return None

    def _on_song(self, vk_id: int, st: dict, text: str, command: str):
        if command == "finale":
            st["phase"] = "finale"
            return [send(*render.finale(self.db.done_topics(vk_id)))]
        if command == "next_location":
            done = self.db.done_topics(vk_id)
            if len(done) >= len(content.TOPICS):
                st["phase"] = "finale"
                return [send(*render.finale(done))]
            return self._select_topic(vk_id, st, self._next_topic_id(done), "story")
        return None

    def _on_finale(self, vk_id: int, st: dict, text: str, command: str):
        if command == "nostalgia":
            return self._place_list(vk_id, st)
        return None
