"""Прогон бота в консоли: без VK, токена и риска для аккаунта.

    python simulate.py                   # интерактивный диалог (пишите как в VK)
    python simulate.py --auto            # автопрогон всего сюжета с верными ответами
    python simulate.py --auto --wrong    # прогон с ошибками (фидбэк и отработка)
    python simulate.py --auto --mode all # сюжет + места + тренировка по темам
    python simulate.py --auto --mode train --topic 7   # тренировка одной темы
    python simulate.py --db sim.db       # сохранять прогресс в файл

Движок тот же, что и в main.py, поэтому прогон проверяет настоящий сценарий.
"""

import argparse
import sys

import content
from bot import texts
from bot.engine import Engine
from db import Database

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BAR = "─" * 60


# ---------- вывод ----------


def print_actions(actions: list, quiet: bool = False) -> None:
    if quiet:
        return
    for action in actions:
        mark = "⟳ (обновлено)" if action.get("edit") else "→"
        print("{} {}".format(mark, action["text"]))
        for row in _rows(action.get("keyboard")):
            print("     [{}]".format("] [".join(row)))
        print()


def _rows(keyboard: dict) -> list:
    if not keyboard:
        return []
    return [[button["action"]["label"] for button in row]
            for row in keyboard.get("buttons", [])]


def last_keyboard(actions: list):
    for action in reversed(actions):
        if action.get("keyboard"):
            return action["keyboard"]
    return None


def pick(keyboard: dict, preferences: list):
    labels = [label for row in _rows(keyboard) for label in row]
    for preferred in preferences:
        if preferred in labels:
            return preferred
    return None


# ---------- автопилот ----------

PREFERENCES = {
    "menu": [texts.BTN_STORY],
    "place": [texts.BTN_LISTEN, texts.BTN_TO_TASKS],
    "theory": [texts.BTN_NEXT, texts.BTN_TO_TASKS],
    "feedback": [texts.BTN_NEXT],
    "song": [texts.BTN_NEXT_LOCATION, texts.BTN_FINALE],
}


def topic_label(nr: int) -> str:
    for topic in content.TOPICS:
        if topic["nr"] == nr:
            return "{}. {}".format(topic["nr"], topic["short"])
    raise KeyError("Тема с номером {} не найдена".format(nr))


def solve_task(st: dict, wrong_mode: bool, counter: int) -> list:
    """Возвращает последовательность нажатий для текущего задания."""
    topic = content.get_topic(st["topic"])
    item = st["queue"][st["qi"]]
    exercise = content.find_exercise(topic, item["id"])
    variant = content.variant(exercise, bool(item.get("retry")))
    mechanics = content.kind_mechanics(variant["kind"])
    make_wrong = wrong_mode and counter % 2 == 0

    if mechanics == "choice":
        index = variant["answer"]
        if make_wrong:
            index = next(i for i in range(len(variant["options"]))
                         if i != variant["answer"])
        return [variant["options"][index]]

    if mechanics == "order":
        words = list(variant["words"])
        if make_wrong:
            words.reverse()
        return words + [texts.BTN_CHECK]

    if st.get("step", 1) == 2 and variant.get("fix"):
        fix = variant["fix"]
        index = fix["answer"]
        if make_wrong:
            index = next(i for i in range(len(fix["options"]))
                         if i != fix["answer"])
        return [fix["options"][index]]

    words = variant["sentence"].split()
    if make_wrong:
        return [next(word for word in words
                     if texts.normalize(word) != texts.normalize(variant["wrong"]))]
    return [variant["wrong"]]


def auto_play(db, engine, vk_id: int, mode: str, wrong_mode: bool,
              quiet: bool, topic_nr: int = 1, limit: int = 900) -> None:
    pending = ["начать"]
    if mode == "story":
        pending.append(texts.BTN_STORY)
    elif mode == "train":
        pending.extend([texts.BTN_TRAIN, topic_label(topic_nr)])
    elif mode == "nostalgia":
        pending.extend([texts.BTN_NOSTALGIA, topic_label(topic_nr)])
    else:
        raise ValueError("Неизвестный режим: {}".format(mode))

    counter = 0
    steps = 0
    retried = set()
    while pending and steps < limit:
        text = pending.pop(0)
        steps += 1
        if not pending:
            counter += 1
        actions = engine.handle(vk_id, text)
        print_actions(actions, quiet)
        if pending:
            continue
        st = db.get_state(vk_id)
        phase = st.get("phase", "menu")
        if phase == "finale":
            break
        if phase == "result":
            keyboard = last_keyboard(actions)
            if wrong_mode and texts.BTN_RETRY_MISTAKES not in retried:
                label = pick(keyboard, [texts.BTN_RETRY_MISTAKES])
                if label:
                    retried.add(texts.BTN_RETRY_MISTAKES)
                    pending.append(label)
                    continue
            break
        if phase == "retry_offer":
            preferred = (texts.BTN_RETRY_MISTAKES if wrong_mode
                         else texts.BTN_SKIP_RETRY)
            label = pick(last_keyboard(actions), [preferred, texts.BTN_SKIP_RETRY,
                                                  texts.BTN_RETRY_MISTAKES])
            if label:
                pending.append(label)
            continue
        if phase == "task":
            pending.extend(solve_task(st, wrong_mode, counter))
            continue
        label = pick(last_keyboard(actions), PREFERENCES.get(phase, []))
        if label:
            pending.append(label)
        else:
            if not quiet:
                print("!! Автопилот не знает, что нажать на фазе {!r}".format(phase))
            break


# ---------- интерактивный режим ----------


def interactive(db, engine, vk_id: int) -> None:
    print(BAR)
    print("Прогон бота в консоли. Пишите текст («Меню», «Сюжет», ответ) или "
          "нажимайте кнопки.\nВыход — слово exit.")
    print(BAR)
    print_actions(engine.handle(vk_id, "/start"))
    while True:
        try:
            text = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if text.lower() in ("exit", "quit", "выход"):
            break
        print_actions(engine.handle(vk_id, text))


# ---------- запуск ----------


def main() -> int:
    parser = argparse.ArgumentParser(description="Прогон бота «Бард» без VK")
    parser.add_argument("--auto", action="store_true", help="автопрогон без ввода")
    parser.add_argument("--wrong", action="store_true",
                        help="в автопрогоне отвечать с ошибками")
    parser.add_argument("--mode", default="story",
                        choices=["story", "train", "nostalgia", "all"],
                        help="что именно прогонять (по умолчанию сюжет)")
    parser.add_argument("--topic", type=int, default=1,
                        help="номер темы для режимов train и nostalgia")
    parser.add_argument("--db", default=":memory:", help="файл базы или :memory:")
    parser.add_argument("--quiet", action="store_true",
                        help="в автопрогоне не печатать диалог")
    parser.add_argument("--vk-id", type=int, default=1, help="условный id игрока")
    args = parser.parse_args()

    try:
        topic_label(args.topic)
    except KeyError as exc:
        parser.error(str(exc))
        return 2

    db = Database(args.db)
    engine = Engine(db)

    if not args.auto:
        interactive(db, engine, args.vk_id)
    else:
        modes = ["story", "nostalgia", "train"] if args.mode == "all" else [args.mode]
        for mode in modes:
            print(BAR)
            print("Автопрогон: режим {}, ответы {}. Прогресс: {}".format(
                mode, "с ошибками" if args.wrong else "верные",
                content.summary()))
            print(BAR)
            auto_play(db, engine, args.vk_id, mode, args.wrong, args.quiet,
                      topic_nr=args.topic)
            done = db.done_topics(args.vk_id)
            stats = db.overall_stats(args.vk_id)
            print("Итог: локаций пройдено {}/{}, решено {}, ошибок {}, "
                  "незакрытых ошибок {}".format(
                      len(done), len(content.TOPICS), stats["correct"],
                      stats["wrong"], stats["unresolved"]))
            print()

    db.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
