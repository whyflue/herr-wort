"""Отрисовка экранов: текст сообщения + клавиатура.

Здесь нет логики состояний — только сборка того, что видит пользователь.
VK не поддерживает markdown, поэтому оформление — эмодзи, кавычки и линии.
Функции возвращают пару (текст, клавиатура-VK).
"""

from bot import keyboards, texts
from content import (
    BALLAD_INTRO,
    BALLAD_TITLE,
    TOPICS,
    kind_hint,
    kind_title,
)

BAR = "─" * 18


def _topic_label(topic: dict, done: bool) -> str:
    label = "{}. {}".format(topic["nr"], topic["short"])
    if done:
        label += " ✅"
    return label


def main_menu(done_count: int, started: bool, complete: bool) -> tuple:
    text = (
        "🎻 БАРД-НОВИЧОК\n"
        "{}\n\n"
        "Привет! Я бард, который мечтает сложить балладу, но пока путается "
        "в немецких словах. Помоги мне: в каждой локации ждёт одна "
        "грамматическая тема A1–A2, а за работу — новая строчка песни.\n\n"
        "Локаций пройдено: {} из {}. Строф в балладе: {}.".format(
            BAR, done_count, len(TOPICS), done_count
        )
    )
    rows = [
        [texts.BTN_STORY, texts.BTN_TRAIN],
        [texts.BTN_STATS, texts.BTN_HELP],
    ]
    if complete:
        rows.append([texts.BTN_NOSTALGIA])
    if started and not complete:
        rows.append([texts.BTN_RESTART])
    return text, keyboards.build(rows)


def help_screen() -> tuple:
    text = (
        "❓ КАК ИГРАТЬ\n"
        "{}\n\n"
        "В боте два режима.\n\n"
        "📖 СЮЖЕТ — путь барда по городам. В каждой локации сначала можно "
        "«прислушаться» и прочитать правило, потом — задания. Ошибка звучит "
        "как фальшивая нота: бот объясняет правило и показывает верный ответ. "
        "Перед новой локацией бард предлагает отработать сложные места — "
        "это похожие задания по тем же правилам. За пройденную тему бард "
        "дописывает строчку баллады.\n\n"
        "🎯 ТРЕНИРОВКА ПО ТЕМАМ — то же самое, но без сюжета: выбираешь тему "
        "из списка и проходишь её сколько угодно раз.\n\n"
        "Задания решаются кнопками: нажми вариант ответа, а если нужно собрать "
        "предложение — нажимай слова по порядку и затем «Проверить». Если кнопки "
        "не видны, всё то же можно набрать словами: «меню», «дальше», «проверить», "
        "«меню».\n\n"
        "Прогресс сохраняется: строфы баллады, статистика и список ошибок, "
        "которые ещё не отработаны. Начать сюжет заново можно в любой момент."
    ).format(BAR)
    return text, keyboards.build([[texts.BTN_MENU]])


def stats_screen(overall: dict, done_ids: list, results: dict) -> tuple:
    lines = [
        "📊 ТВОИ РЕЗУЛЬТАТЫ",
        BAR,
        "Решено заданий: {}, ошибок: {} → точность {}%".format(
            overall["correct"] + overall["wrong"],
            overall["wrong"],
            overall["accuracy"],
        ),
        "Подходов к темам: {}".format(overall["attempts"]),
        "Локаций пройдено: {} из {}".format(len(done_ids), len(TOPICS)),
        "Незакрытых ошибок: {}".format(overall["unresolved"]),
        "",
        "ПО ТЕМАМ:",
    ]
    for topic in TOPICS:
        result = results.get(topic["id"]) or {}
        mark = "✅" if topic["id"] in done_ids else "·"
        best = result.get("best")
        if best is None:
            lines.append("{} {}. {} — ещё не решал".format(
                mark, topic["nr"], topic["short"]))
        else:
            lines.append("{} {}. {} — лучший результат {}% (попыток: {})".format(
                mark, topic["nr"], topic["short"], best, result.get("attempts", 0)))
    return "\n".join(lines), keyboards.build([[texts.BTN_MENU]])


def story_intro() -> tuple:
    text = (
        "📖 СЮЖЕТ: ПУТЬ БАРДА\n"
        "{}\n\n"
        "Бард-новичок идёт через немецкие земли: от рынка Любека до собора "
        "в Аахене. В каждой локации он разбирает одну тему и дописывает "
        "строчку баллады. Пока строф мало — но так и начинается песня.\n\n"
        "Первая остановка — Любек, рыночная площадь."
    ).format(BAR)
    return text, keyboards.build([[texts.BTN_MENU]])


def place(topic: dict, ctx: str) -> tuple:
    if ctx == "nostalgia":
        header = "🏰 ВОСПОМИНАНИЕ: {}".format(topic["location"])
        tail = "Бард идёт по знакомым местам — здесь когда-то родилась строфа."
    elif ctx == "train":
        header = "🎯 ТРЕНИРОВКА — {}\n🎼 Тема: {} ({})".format(
            topic["location"], topic["title"], topic["title_de"])
        tail = "Сюжет отдыхает: слушаем правило и решаем задания."
    else:
        header = "📍 ЛОКАЦИЯ {} ИЗ {} — {}\n🎼 Тема: {} ({})".format(
            topic["nr"], len(TOPICS), topic["location"],
            topic["title"], topic["title_de"])
        tail = "Впереди — звуки места и задания."
    text = "{}\n{}\n\n{}\n\n{}".format(header, BAR, topic["intro"], tail)
    rows = [[texts.BTN_LISTEN, texts.BTN_TO_TASKS]]
    if ctx == "train":
        rows.append([texts.BTN_TO_TOPICS])
    elif ctx == "nostalgia":
        rows.append([texts.BTN_TO_PLACES])
    rows.append([texts.BTN_MENU])
    return text, keyboards.build(rows)


def theory_page(topic: dict, page_index: int, ctx: str) -> tuple:
    pages = topic["theory"]
    page = pages[page_index]
    total = len(pages)
    head = "📖 ТЕОРИЯ: {} — {}\n{}".format(topic["title"], page["title"], BAR)
    if page_index == 0:
        head = "🎧 {}\n\n{}".format(topic["listen"], head)
    last = page_index + 1 >= total
    tail = ("Правило записано — можно пробовать." if last
            else "Листай дальше, чтобы узнать правило целиком.")
    text = "{}\n📄 Страница {} из {}\n\n{}\n\n{}\n\n{}".format(
        head, page_index + 1, total, page["body"], BAR, tail)
    rows = []
    if not last:
        rows.append([texts.BTN_NEXT])
    rows.append([texts.BTN_TO_TASKS])
    rows.append([texts.BTN_MENU])
    return text, keyboards.build(rows)


def task(topic: dict, exercise: dict, index: int, total: int,
         build: list = None, step: int = 1, is_retry: bool = False) -> tuple:
    """Экран задания. build — собранные слова для kind=order."""
    kind = exercise["kind"]
    build = build or []
    head = "✍️ Задание {} из {}".format(index, total)
    if is_retry:
        head += " (отработка)"
    lines = [head, "📍 {}".format(topic["location"]), BAR,
             kind_title(kind), ""]

    if kind == "order":
        sentence = " ".join(build) if build else "…"
        lines.append(exercise["prompt"])
        lines.append("")
        lines.append("Собрано: {}".format(sentence))
        lines.append("")
        lines.append(_hint(kind_hint(kind)) + ".")
        rows = keyboards.pack(exercise["words"], per_row=3)
        rows.append([texts.BTN_UNDO, texts.BTN_CHECK])
        rows.append([texts.BTN_CLEAR, texts.BTN_MENU])
        return "\n".join(lines), keyboards.build(rows)

    if kind == "error" and step == 1:
        lines.append(exercise["prompt"])
        lines.append("")
        lines.append(exercise["sentence"])
        rows = keyboards.pack(exercise["sentence"].split(), per_row=3)
        rows.append([texts.BTN_MENU])
        return "\n".join(lines), keyboards.build(rows)

    if kind == "error" and step == 2:
        lines.append("Ошибка найдена: «{}». Как исправить?".format(exercise["wrong"]))
        lines.append("")
        lines.append(exercise["sentence"])
        rows = keyboards.single_row_options(exercise["fix"]["options"])
        rows.append([texts.BTN_MENU])
        return "\n".join(lines), keyboards.build(rows)

    lines.append(exercise["prompt"])
    lines.append("")
    lines.append(_hint(kind_hint(kind)) + ".")
    rows = keyboards.single_row_options(exercise["options"])
    rows.append([texts.BTN_MENU])
    return "\n".join(lines), keyboards.build(rows)


def feedback(exercise: dict, kind: str, ok: bool, right: str,
             is_retry: bool = False) -> tuple:
    if ok:
        head = "🎵 Верно!" if not is_retry else "🎵 Верно — вот и рифма нашлась!"
        if kind == "order":
            head += "\n\nТвоё предложение: {}".format(right)
    else:
        head = ("🎼 Фальшивая нота!\n\n"
                "Ладонь барда сбивается со струн. Правильный ответ: {}".format(right))
    text = "{}\n{}\n\n{}\n\n{}".format(head, BAR, exercise.get("explain", ""), BAR)
    rows = [[texts.BTN_NEXT], [texts.BTN_MENU]]
    return text, keyboards.build(rows)


def error_step_feedback(exercise: dict, ok: bool, tapped: str) -> tuple:
    """Подсказка после первого шага «найди ошибку» (используется движком
    при неверном нажатии слова)."""
    if ok:
        text = ("🔍 Точно: слово «{}» здесь неверно.\n{}".format(
            exercise["wrong"], BAR))
    else:
        text = ("🔍 Нет, со словом «{}» всё в порядке.\n"
                "Ошибка — в слове «{}».".format(tapped, exercise["wrong"]))
    return text, None


def _hint(text: str) -> str:
    return text[0].upper() + text[1:] if text else text


def retry_offer(topic: dict, mistakes: list) -> tuple:
    text = (
        "🔁 БАРД ЗАБЫЛ РИФМУ\n"
        "{}\n\n"
        "За поворотом дороги бард останавливается: рифма потерялась, и {} "
        "из последних заданий прозвучали фальшиво. Вернёмся к этим правилам? "
        "Бот даст похожие задания — то же правило, другой пример.\n\n"
        "Тема: {}".format(BAR, len(mistakes), topic["title"])
    )
    rows = [
        [texts.BTN_RETRY_MISTAKES],
        [texts.BTN_SKIP_RETRY],
        [texts.BTN_MENU],
    ]
    return text, keyboards.build(rows)


def song(topic: dict, done_count: int, complete: bool) -> tuple:
    text = (
        "🎶 НОВАЯ СТРОФА!\n"
        "{}\n\n"
        "Бард останавливается, достаёт перо и дописывает в свиток:\n\n"
        "🎵 {}\n\n"
        "Строф в балладе: {} из {}.".format(
            BAR, topic["song_line"], done_count, len(TOPICS))
    )
    if not complete:
        text += "\n\nВпереди — новый город и новая тема."
    rows = [[texts.BTN_FINALE if complete else texts.BTN_NEXT_LOCATION],
            [texts.BTN_MENU]]
    return text, keyboards.build(rows)


def finale(done_ids: list) -> tuple:
    lines = [
        "🏁 БАЛЛАДА ДОПИСАНА!",
        BAR,
        "Бард выходит на площадь и поёт от начала до конца — {} строф "
        "о городах, людях и правилах, которые дались не сразу.".format(len(TOPICS)),
        "",
        "🎶 «{}»".format(BALLAD_TITLE),
        BALLAD_INTRO,
        "",
    ]
    for topic in TOPICS:
        if topic["id"] in done_ids:
            lines.append("{}. {}".format(topic["nr"], topic["short"]))
            lines.append(topic["song_line"])
            lines.append("")
    lines.append(
        "Где пелось — там и вспоминается легче. Бард может вернуться в любое "
        "место и повторить его правило, а может начать весь путь заново и "
        "спеть другую балладу."
    )
    rows = [
        [texts.BTN_NOSTALGIA],
        [texts.BTN_RESTART],
        [texts.BTN_MENU],
    ]
    return "\n".join(lines), keyboards.build(rows)


def topic_list(done_ids: list) -> tuple:
    text = (
        "🎯 ТРЕНИРОВКА ПО ТЕМАМ\n"
        "{}\n\n"
        "Сюжет здесь не нужен: выбирай тему, слушай правило и решай задания. "
        "Отметкой ✅ помечены темы, пройденные в сюжете.".format(BAR)
    )
    labels = [_topic_label(topic, topic["id"] in done_ids) for topic in TOPICS]
    rows = [labels[i:i + 2] for i in range(0, len(labels), 2)]
    rows.append([texts.BTN_MENU])
    return text, keyboards.build(rows)


def place_list(done_ids: list) -> tuple:
    text = (
        "🏰 ГДЕ ПИСАЛАСЬ БАЛЛАДА\n"
        "{}\n\n"
        "Бард идёт по знакомым местам: где-то пахнет хлебом, где-то слышны "
        "колокола. Выбери место — и вспомни правило, которое в нём родилось.".format(BAR)
    )
    labels = [
        _topic_label(topic, True)
        for topic in TOPICS if topic["id"] in done_ids
    ]
    rows = [labels[i:i + 2] for i in range(0, len(labels), 2)]
    rows.append([texts.BTN_MENU])
    return text, keyboards.build(rows)


def result(topic: dict, correct: int, wrong: int, ctx: str) -> tuple:
    total = correct + wrong
    percent = round(correct / total * 100) if total else 0
    if percent >= 80:
        verdict = "Бард доволен: тема звучит уверенно."
    elif percent < 60:
        verdict = "Бард хмурится: правило ещё шатается."
    else:
        verdict = "Почти чисто — осталось закрепить пару мест."
    text = (
        "📊 РЕЗУЛЬТАТ\n"
        "{}\n"
        "Тема: {} ({})\n"
        "Верно: {} из {} — {}%\n"
        "Фальшивых нот: {}\n\n"
        "{}".format(BAR, topic["title"], topic["title_de"],
                    correct, total, percent, wrong, verdict)
    )
    rows = []
    if wrong:
        rows.append([texts.BTN_RETRY_MISTAKES])
    rows.append([
        texts.BTN_AGAIN,
        texts.BTN_TO_PLACES if ctx == "nostalgia" else texts.BTN_TO_TOPICS,
    ])
    rows.append([texts.BTN_MENU])
    return text, keyboards.build(rows)


def restart_confirm() -> tuple:
    text = (
        "🔄 НАЧАТЬ СЮЖЕТ ЗАНОВО?\n"
        "{}\n\n"
        "Бард порвёт свиток и вернётся в Любек: строфы баллады сбросятся, "
        "локации откроются заново. История ошибок и статистика сохранятся — "
        "они пригодятся в тренировке.".format(BAR)
    )
    rows = [[texts.BTN_RESTART_YES], [texts.BTN_RESTART_NO]]
    return text, keyboards.build(rows)


def fallback() -> tuple:
    text = (
        "🤔 Похоже, это не команда. Нажимай кнопки под сообщением — "
        "или выбери, куда идти дальше."
    )
    return text, keyboards.build([[texts.BTN_MENU], [texts.BTN_HELP]])
