"""Отрисовка экранов: текст сообщения + клавиатура.

Здесь нет логики состояний — только сборка того, что видит пользователь.
VK не поддерживает markdown, поэтому оформление — эмодзи, кавычки и линии.
Функции возвращают пару (текст, клавиатура-VK).

Все содержательные тексты двуязычны: сначала немецкий, затем русский
(🇩🇪/🇷🇺). Это относится и к сюжетным описаниям, и к подсказкам, и к
разбору заданий.
"""

import random

from bot import keyboards, texts
from content import (
    BALLAD_INTRO,
    BALLAD_INTRO_DE,
    BALLAD_TITLE,
    BALLAD_TITLE_DE,
    TOPICS,
    kind_hint,
    kind_mechanics,
    kind_title,
    prompt_de,
    wrong_words,
)

BAR = "─" * 18


def topic_label(topic: dict, done: bool) -> str:
    """Подпись темы для кнопок: сначала немецкое, затем русское название."""
    short_de = topic.get("short_de") or topic["short"]
    label = "{}. {}".format(topic["nr"], short_de)
    if topic.get("short"):
        label += " / {}".format(topic["short"])
    if done:
        label += " ✅"
    return label


def main_menu(done_count: int, started: bool, complete: bool) -> tuple:
    text = (
        "🎻 DER ANFÄNGER-BARDE / БАРД-НОВИЧОК\n"
        "{}\n\n"
        "{}\n\n"
        "{}\n\n"
        "{}".format(
            BAR,
            texts.bi(
                "Hallo! Ich bin ein Barde, der eine Ballade dichten möchte, aber "
                "noch über die deutschen Wörter stolpert. Hilf mir: An jedem "
                "Ort wartet ein Grammatikthema (A1–A2), und für die Arbeit "
                "gibt es eine neue Liedzeile.",
                "Привет! Я бард, который мечтает сложить балладу, но пока "
                "путается в немецких словах. Помоги мне: в каждой локации "
                "ждёт одна грамматическая тема A1–A2, а за работу — новая "
                "строчка песни.",
            ),
            texts.bi(
                "Geschaffte Orte: {} von {}. Strophen in der Ballade: {}.".format(
                    done_count, len(TOPICS), done_count),
                "Локаций пройдено: {} из {}. Строф в балладе: {}.".format(
                    done_count, len(TOPICS), done_count),
            ),
            texts.bi(
                "Bitte füllt nach dem Durchspielen den Feedback-Fragebogen "
                "aus — die Schaltfläche „Feedback“ öffnet ihn.",
                "Заполните, пожалуйста, анкету с обратной связью после "
                "прохождения бота — её откроет кнопка «Обратная связь».",
            ),
        )
    )
    rows = [
        [texts.BTN_STORY, texts.BTN_TRAIN],
        [texts.BTN_STATS, texts.BTN_HELP],
        [texts.BTN_FEEDBACK],
    ]
    if complete:
        rows.append([texts.BTN_NOSTALGIA])
    if started and not complete:
        rows.append([texts.BTN_RESTART])
    return text, keyboards.build(rows)


def help_screen() -> tuple:
    de = (
        "Im Bot gibt es zwei Modi.\n\n"
        "📖 HANDLUNG — der Weg des Barden durch die Städte. An jedem Ort kann "
        "man zuerst „lauschen“ und die Regel lesen; vor den Aufgaben bietet "
        "der Bot selbst die Wahl an: die Regel zeigen oder ohne sie beginnen. "
        "Regeln und Erklärungen gibt es auf Deutsch und Russisch. Ein Fehler "
        "klingt wie ein falscher Ton: Der Bot zeigt die richtige Antwort und "
        "erklärt sie in beiden Sprachen. Vor einem neuen Ort bietet der Barde "
        "an, die Aufgaben zu wiederholen, bei denen es Fehler gab. Für ein "
        "geschafftes Thema schreibt der Barde eine neue Zeile der Ballade.\n\n"
        "🎯 THEMEN-TRAINING — dasselbe, aber ohne Handlung: Du wählst ein "
        "Thema aus der Liste und übst es so oft du willst.\n\n"
        "Aufgaben löst man mit Schaltflächen oder als Text: Klicke eine "
        "Antwort an; wenn ein Wort oder eine Phrase geschrieben werden muss, "
        "schicke die Antwort als Nachricht (Groß- und Kleinschreibung und "
        "Umlaute sind nicht wichtig); wenn ein Satz gebaut werden soll, "
        "klicke die Wörter der Reihe nach an und dann „Prüfen“. Befehle "
        "kann man auch als Wörter schreiben: „Menü“, „Weiter“, „Prüfen“.\n\n"
        "Der Fortschritt wird gespeichert: die Strophen der Ballade, die "
        "Statistik und die Liste der Fehler, die noch nicht geübt sind. Die "
        "Handlung kann man jederzeit neu beginnen."
    )
    ru = (
        "В боте два режима.\n\n"
        "📖 СЮЖЕТ — путь барда по городам. В каждой локации можно сначала "
        "«прислушаться» и прочитать правило, а перед заданиями бот сам "
        "предлагает выбрать: показать правило или начать без него. Правила "
        "и объяснения даются на двух языках — по-немецки и по-русски. Ошибка "
        "звучит как фальшивая нота: бот показывает верный ответ и объясняет "
        "его на обоих языках. Перед новой локацией бард предлагает повторить "
        "задания, где были ошибки. За пройденную тему бард дописывает строчку "
        "баллады.\n\n"
        "🎯 ТРЕНИРОВКА ПО ТЕМАМ — то же самое, но без сюжета: выбираешь тему "
        "из списка и проходишь её сколько угодно раз.\n\n"
        "Задания решаются кнопками или текстом: нажми вариант ответа; если "
        "нужно написать слово или фразу — отправь ответ сообщением (регистр "
        "и умляуты не важны); а если нужно собрать предложение — нажимай "
        "слова по порядку и затем «Проверить». Команды можно набирать "
        "словами: «меню», «дальше», «проверить».\n\n"
        "Прогресс сохраняется: строфы баллады, статистика и список ошибок, "
        "которые ещё не отработаны. Начать сюжет заново можно в любой момент."
    )
    text = "❓ WIE MAN SPIELT / КАК ИГРАТЬ\n{}\n\n{}".format(
        BAR, texts.bi(de, ru))
    return text, keyboards.build([[texts.BTN_MENU]])


def stats_screen(overall: dict, done_ids: list, results: dict) -> tuple:
    de_lines = [
        "📊 DEINE ERGEBNISSE",
        BAR,
        "Gelöste Aufgaben: {}, Fehler: {} → Genauigkeit {}%".format(
            overall["correct"] + overall["wrong"],
            overall["wrong"],
            overall["accuracy"],
        ),
        "Themenversuche: {}".format(overall["attempts"]),
        "Geschaffte Orte: {} von {}".format(len(done_ids), len(TOPICS)),
        "Offene Fehler: {}".format(overall["unresolved"]),
        "",
        "NACH THEMEN:",
    ]
    ru_lines = [
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
        de_short = topic.get("short_de") or topic["short"]
        if best is None:
            de_lines.append("{} {}. {} — noch nicht geübt".format(
                mark, topic["nr"], de_short))
            ru_lines.append("{} {}. {} — ещё не решал".format(
                mark, topic["nr"], topic["short"]))
        else:
            de_lines.append(
                "{} {}. {} — bestes Ergebnis {}% (Versuche: {})".format(
                    mark, topic["nr"], de_short, best,
                    result.get("attempts", 0)))
            ru_lines.append(
                "{} {}. {} — лучший результат {}% (попыток: {})".format(
                    mark, topic["nr"], topic["short"], best,
                    result.get("attempts", 0)))
    text = texts.bi("\n".join(de_lines), "\n".join(ru_lines))
    return text, keyboards.build([[texts.BTN_MENU]])


def story_intro() -> tuple:
    text = (
        "📖 HANDLUNG: DER WEG DES BARDEN / СЮЖЕТ: ПУТЬ БАРДА\n"
        "{}\n\n"
        "{}\n\n"
        "{}".format(
            BAR,
            texts.bi(
                "Der Anfänger-Barde zieht durch deutsche Lande: vom Markt in "
                "Lübeck bis zum Dom in Aachen. An jedem Ort behandelt er ein "
                "Thema und schreibt eine Zeile der Ballade. Noch sind es "
                "wenige Strophen — aber so beginnt ein Lied.",
                "Бард-новичок идёт через немецкие земли: от рынка Любека до "
                "собора в Аахене. В каждой локации он разбирает одну тему и "
                "дописывает строчку баллады. Пока строф мало — но так и "
                "начинается песня.",
            ),
            texts.bi(
                "Die erste Station ist Lübeck, der Marktplatz.",
                "Первая остановка — Любек, рыночная площадь.",
            ),
        )
    )
    return text, keyboards.build([[texts.BTN_MENU]])


def place(topic: dict, ctx: str) -> tuple:
    location_de = topic.get("location_de") or topic["location"]
    if ctx == "nostalgia":
        header = "🏰 ERINNERUNG: {}\n🇷🇺 ВОСПОМИНАНИЕ: {}".format(
            location_de, topic["location"])
        tail_de = ("Der Barde geht durch vertraute Orte — hier entstand einst "
                   "eine Strophe.")
        tail_ru = ("Бард идёт по знакомым местам — здесь когда-то родилась "
                   "строфа.")
    elif ctx == "train":
        header = (
            "🎯 THEMEN-TRAINING — {}\n🇷🇺 ТРЕНИРОВКА — {}\n"
            "🎼 Thema: {}\n🇷🇺 Тема: {}".format(
                location_de, topic["location"], topic["title_de"], topic["title"])
        )
        tail_de = "Die Handlung ruht: Wir hören die Regel und lösen Aufgaben."
        tail_ru = "Сюжет отдыхает: слушаем правило и решаем задания."
    else:
        header = (
            "📍 STATION {} VON {} — {}\n"
            "🇷🇺 ЛОКАЦИЯ {} ИЗ {} — {}\n"
            "🎼 Thema: {}\n"
            "🇷🇺 Тема: {}".format(
                topic["nr"], len(TOPICS), location_de,
                topic["nr"], len(TOPICS), topic["location"],
                topic["title_de"], topic["title"])
        )
        tail_de = "Vor uns liegen die Klänge des Ortes und die Aufgaben."
        tail_ru = "Впереди — звуки места и задания."
    text = "{}\n{}\n\n{}\n\n{}".format(
        header,
        BAR,
        texts.bi(topic.get("intro_de", ""), topic["intro"]),
        texts.bi(tail_de, tail_ru),
    )
    rows = [[texts.BTN_LISTEN, texts.BTN_TO_TASKS]]
    if ctx == "train":
        rows.append([texts.BTN_TO_TOPICS])
    elif ctx == "nostalgia":
        rows.append([texts.BTN_TO_PLACES])
    rows.append([texts.BTN_MENU])
    return text, keyboards.build(rows)


def rule_choice(topic: dict, ctx: str) -> tuple:
    text = (
        "📖 REGEL VOR DEN AUFGABEN / ПРАВИЛО ПЕРЕД ЗАДАНИЯМИ\n"
        "{}\n\n"
        "🎼 Thema: {} / Тема: {}\n\n"
        "{}".format(
            BAR,
            topic["title_de"], topic["title"],
            texts.bi(
                "Die Regel öffnet sich auf Deutsch und Russisch. Du kannst sie "
                "zuerst auffrischen — oder gleich zu den Aufgaben gehen: Die "
                "Erklärung erscheint trotzdem, wenn die Antwort falsch ist.",
                "Правило откроется сразу на двух языках — по-немецки и "
                "по-русски. Можно сначала освежить его — или сразу перейти к "
                "заданиям: объяснение всё равно появится, если ответ "
                "окажется неверным.",
            ),
        )
    )
    rows = [
        [texts.BTN_SHOW_RULE],
        [texts.BTN_START_NO_RULE],
        [texts.BTN_MENU],
    ]
    return text, keyboards.build(rows)


def theory_page(topic: dict, page_index: int, ctx: str) -> tuple:
    pages = topic["theory"]
    page = pages[page_index]
    total = len(pages)
    head = "📖 THEORIE: {}\n🇷🇺 ТЕОРИЯ: {}\n{}".format(
        topic["title_de"], topic["title"], BAR)
    if page_index == 0:
        head = "🎧 {}\n\n{}".format(
            texts.bi(topic.get("listen_de", ""), topic["listen"]), head)
    last = page_index + 1 >= total
    tail_de = ("Die Regel ist notiert — du kannst es versuchen." if last
               else "Blättere weiter, um die ganze Regel zu sehen.")
    tail_ru = ("Правило записано — можно пробовать." if last
               else "Листай дальше, чтобы узнать правило целиком.")
    text = (
        "{}\n"
        "📄 Seite {} von {} / Страница {} из {}\n\n"
        "{}\n\n"
        "{}\n\n"
        "{}"
    ).format(
        head,
        page_index + 1, total, page_index + 1, total,
        texts.bi(page.get("title_de", ""), page["title"], block=False),
        texts.bi(page["body_de"], page["body"]),
        texts.bi(tail_de, tail_ru),
    )
    rows = []
    if not last:
        rows.append([texts.BTN_NEXT])
    rows.append([texts.BTN_TO_TASKS])
    rows.append([texts.BTN_MENU])
    return text, keyboards.build(rows)


def _shuffled_words(exercise: dict) -> list:
    """Перемешивает слова для сборки, но всегда одинаково для одного задания.

    В самих данных `words` хранятся в правильном порядке: так validator
    сверяет `answer` и так автопилот собирает предложение. На экран слова
    отдаются перемешанными, иначе задание решалось бы нажатиями слева
    направо.
    """
    words = list(exercise["words"])
    if len(set(words)) < 2:
        return words
    rng = random.Random("order:" + exercise["id"])
    shuffled = list(words)
    for _ in range(10):
        rng.shuffle(shuffled)
        if shuffled != words:
            return shuffled
    return shuffled


def _prompt(exercise: dict) -> str:
    """Условие задания: немецкий перевод ставим перед русской инструкцией."""
    de = prompt_de(exercise)
    if de:
        return texts.bi(de, exercise["prompt"], block=False)
    return exercise["prompt"]


def task(topic: dict, exercise: dict, index: int, total: int,
         build: list = None, step: int = 1, is_retry: bool = False) -> tuple:
    """Экран задания. build — собранные слова для kind=order."""
    kind = exercise["kind"]
    build = build or []
    head_de = "✍️ Aufgabe {} von {}".format(index, total)
    head_ru = "✍️ Задание {} из {}".format(index, total)
    if is_retry:
        head_de += " (Wiederholung)"
        head_ru += " (отработка)"
    location_de = topic.get("location_de") or topic["location"]
    lines = [
        texts.bi(head_de, head_ru, block=False),
        "📍 {}\n🇷🇺 {}".format(location_de, topic["location"]),
        BAR,
        texts.bi(kind_title(kind, "de"), kind_title(kind), block=False),
        "",
    ]

    if kind == "order":
        sentence = " ".join(build) if build else "…"
        lines.append(_prompt(exercise))
        lines.append("")
        lines.append("🇩🇪 Gebaut: {}\n🇷🇺 Собрано: {}".format(sentence, sentence))
        lines.append("")
        lines.append(
            texts.bi(_hint(kind_hint(kind, "de")), _hint(kind_hint(kind)),
                     block=False) + ".")
        rows = keyboards.pack(_shuffled_words(exercise), per_row=3)
        rows.append([texts.BTN_UNDO, texts.BTN_CHECK])
        rows.append([texts.BTN_CLEAR, texts.BTN_MENU])
        return "\n".join(lines), keyboards.build(rows)

    if kind == "error" and step == 1:
        lines.append(_prompt(exercise))
        lines.append("")
        lines.append(exercise["sentence"])
        rows = keyboards.pack(exercise["sentence"].split(), per_row=3)
        rows.append([texts.BTN_MENU])
        return "\n".join(lines), keyboards.build(rows)

    if kind == "error" and step == 2:
        found = ", ".join("«{}»".format(word) for word in wrong_words(exercise))
        lines.append(texts.bi(
            "Fehler gefunden: {}. Wie korrigiert man ihn?".format(found),
            "Ошибка найдена: {}. Как исправить?".format(found),
        ))
        lines.append("")
        lines.append(exercise["sentence"])
        rows = keyboards.single_row_options(exercise["fix"]["options"])
        rows.append([texts.BTN_MENU])
        return "\n".join(lines), keyboards.build(rows)

    if kind_mechanics(kind) == "input":
        lines.append(_prompt(exercise))
        lines.append("")
        lines.append(
            texts.bi(_hint(kind_hint(kind, "de")), _hint(kind_hint(kind)),
                     block=False) + ".")
        rows = [[texts.BTN_MENU]]
        return "\n".join(lines), keyboards.build(rows)

    lines.append(_prompt(exercise))
    lines.append("")
    lines.append(
        texts.bi(_hint(kind_hint(kind, "de")), _hint(kind_hint(kind)),
                 block=False) + ".")
    rows = keyboards.single_row_options(exercise["options"])
    rows.append([texts.BTN_MENU])
    return "\n".join(lines), keyboards.build(rows)


def feedback(exercise: dict, kind: str, ok: bool, right: str,
             is_retry: bool = False) -> tuple:
    if ok:
        de_head = "🎵 Richtig!" if not is_retry else "🎵 Richtig — da ist der Reim!"
        ru_head = "🎵 Верно!" if not is_retry else "🎵 Верно — вот и рифма нашлась!"
        if kind == "order":
            de_head += "\n\nDein Satz: {}".format(right)
            ru_head += "\n\nТвоё предложение: {}".format(right)
        elif kind == "error":
            de_head += "\n\nKorrigierter Satz: {}".format(right)
            ru_head += "\n\nИсправленное предложение: {}".format(right)
    else:
        de_head = ("🎼 Falscher Ton!\n\nDie Hand des Barden rutscht über die "
                   "Saiten. Richtige Antwort: {}".format(right))
        ru_head = ("🎼 Фальшивая нота!\n\nЛадонь барда сбивается со струн. "
                   "Правильный ответ: {}".format(right))
    # Объяснение показываем на двух языках: сначала немецкий, затем русский —
    # и при верном, и при неверном ответе.
    body = texts.bi(exercise.get("explain_de", ""), exercise.get("explain", ""))
    text = "{}\n{}\n\n{}\n{}".format(
        texts.bi(de_head, ru_head), BAR, body, BAR)
    rows = [[texts.BTN_NEXT], [texts.BTN_MENU]]
    return text, keyboards.build(rows)


def error_step_feedback(exercise: dict, ok: bool, tapped: str) -> tuple:
    """Подсказка после первого шага «найди ошибку» (используется движком
    при неверном нажатии слова)."""
    words = wrong_words(exercise)
    found = ", ".join("«{}»".format(word) for word in words) or "?"
    if ok:
        text = texts.bi(
            "🔍 Genau: Das Wort «{}» ist hier falsch.".format(tapped),
            "🔍 Точно: слово «{}» здесь неверно.".format(tapped),
        ) + "\n{}".format(BAR)
    else:
        text = texts.bi(
            "🔍 Nein, mit dem Wort «{}» ist alles in Ordnung.\n"
            "Der Fehler steckt in: {}.".format(tapped, found),
            "🔍 Нет, со словом «{}» всё в порядке.\n"
            "Ошибка — в слове {}.".format(tapped, found),
        )
    return text, None


def _hint(text: str) -> str:
    return text[0].upper() + text[1:] if text else text


def retry_offer(topic: dict, mistakes: list) -> tuple:
    text = (
        "🔁 DER BARDE HAT DEN REIM VERGESSEN / БАРД ЗАБЫЛ РИФМУ\n"
        "{}\n\n"
        "🎼 Thema: {} / Тема: {}\n\n"
        "{}".format(
            BAR,
            topic["title_de"], topic["title"],
            texts.bi(
                "Hinter der Wegbiegung hält der Barde an: Der Reim ist "
                "verloren, und {} der letzten Aufgaben klangen falsch. Kehren "
                "wir zu diesen Regeln zurück? Der Bot wiederholt die Aufgaben, "
                "bei denen es Fehler gab.".format(len(mistakes)),
                "За поворотом дороги бард останавливается: рифма потерялась, "
                "и {} из последних заданий прозвучали фальшиво. Вернёмся к "
                "этим правилам? Бот повторит задания, где были "
                "ошибки.".format(len(mistakes)),
            ),
        )
    )
    rows = [
        [texts.BTN_RETRY_MISTAKES],
        [texts.BTN_SKIP_RETRY],
        [texts.BTN_MENU],
    ]
    return text, keyboards.build(rows)


def song(topic: dict, done_count: int, complete: bool) -> tuple:
    text = (
        "🎶 EINE NEUE STROPHE! / НОВАЯ СТРОФА!\n"
        "{}\n\n"
        "{}\n\n"
        "🎵 {}\n\n"
        "{}".format(
            BAR,
            texts.bi(
                "Der Barde hält an, nimmt die Feder und schreibt in die Rolle:",
                "Бард останавливается, достаёт перо и дописывает в свиток:",
            ),
            topic["song_line"],
            texts.bi(
                "Strophen in der Ballade: {} von {}.".format(
                    done_count, len(TOPICS)),
                "Строф в балладе: {} из {}.".format(done_count, len(TOPICS)),
            ),
        )
    )
    if not complete:
        text += "\n\n" + texts.bi(
            "Vor uns liegen eine neue Stadt und ein neues Thema.",
            "Впереди — новый город и новая тема.",
        )
    rows = [[texts.BTN_FINALE if complete else texts.BTN_NEXT_LOCATION],
            [texts.BTN_MENU]]
    return text, keyboards.build(rows)


def finale(done_ids: list) -> tuple:
    lines = [
        "🏁 DIE BALLADE IST FERTIG! / БАЛЛАДА ДОПИСАНА!",
        BAR,
        texts.bi(
            "Der Barde tritt auf den Platz und singt sie von Anfang bis Ende — "
            "{} Strophen über Städte, Menschen und Regeln, die nicht gleich "
            "gelungen sind.".format(len(TOPICS)),
            "Бард выходит на площадь и поёт от начала до конца — {} строф "
            "о городах, людях и правилах, которые дались не сразу.".format(
                len(TOPICS)),
        ),
        "",
        "🎶 «{}» / «{}»".format(BALLAD_TITLE_DE, BALLAD_TITLE),
        texts.bi(BALLAD_INTRO_DE, BALLAD_INTRO),
        "",
    ]
    for topic in TOPICS:
        if topic["id"] in done_ids:
            lines.append("{}. {} / {}".format(
                topic["nr"], topic.get("short_de") or topic["short"],
                topic["short"]))
            lines.append(topic["song_line"])
            lines.append("")
    lines.append(texts.bi(
        "Wo gesungen wurde, erinnert man sich leichter. Der Barde kann an "
        "jeden Ort zurückkehren und seine Regel wiederholen oder den ganzen "
        "Weg neu beginnen und eine andere Ballade singen.",
        "Где пелось — там и вспоминается легче. Бард может вернуться в любое "
        "место и повторить его правило, а может начать весь путь заново и "
        "спеть другую балладу.",
    ))
    rows = [
        [texts.BTN_NOSTALGIA],
        [texts.BTN_RESTART],
        [texts.BTN_MENU],
    ]
    return "\n".join(lines), keyboards.build(rows)


def topic_list(done_ids: list) -> tuple:
    text = (
        "🎯 THEMEN-TRAINING / ТРЕНИРОВКА ПО ТЕМАМ\n"
        "{}\n\n"
        "{}".format(
            BAR,
            texts.bi(
                "Hier braucht man keine Handlung: Wähle ein Thema, höre die "
                "Regel und löse die Aufgaben. ✅ markiert Themen, die in der "
                "Handlung geschafft sind.",
                "Сюжет здесь не нужен: выбирай тему, слушай правило и решай "
                "задания. Отметкой ✅ помечены темы, пройденные в сюжете.",
            ),
        )
    )
    labels = [topic_label(topic, topic["id"] in done_ids) for topic in TOPICS]
    rows = [labels[i:i + 2] for i in range(0, len(labels), 2)]
    rows.append([texts.BTN_MENU])
    return text, keyboards.build(rows)


def place_list(done_ids: list) -> tuple:
    text = (
        "🏰 WO DIE BALLADE GESCHRIEBEN WURDE / ГДЕ ПИСАЛАСЬ БАЛЛАДА\n"
        "{}\n\n"
        "{}".format(
            BAR,
            texts.bi(
                "Der Barde geht durch vertraute Orte: Hier duftet es nach Brot, "
                "dort läuten Glocken. Wähle einen Ort — und erinnere dich an "
                "die Regel, die dort entstanden ist.",
                "Бард идёт по знакомым местам: где-то пахнет хлебом, где-то "
                "слышны колокола. Выбери место — и вспомни правило, которое "
                "в нём родилось.",
            ),
        )
    )
    labels = [
        topic_label(topic, True)
        for topic in TOPICS if topic["id"] in done_ids
    ]
    rows = [labels[i:i + 2] for i in range(0, len(labels), 2)]
    rows.append([texts.BTN_MENU])
    return text, keyboards.build(rows)


def result(topic: dict, correct: int, wrong: int, ctx: str) -> tuple:
    total = correct + wrong
    percent = round(correct / total * 100) if total else 0
    if percent >= 80:
        de_verdict = "Der Barde ist zufrieden: Das Thema klingt sicher."
        ru_verdict = "Бард доволен: тема звучит уверенно."
    elif percent < 60:
        de_verdict = "Der Barde runzelt die Stirn: Die Regel wackelt noch."
        ru_verdict = "Бард хмурится: правило ещё шатается."
    else:
        de_verdict = "Fast sauber — ein paar Stellen müssen noch sitzen."
        ru_verdict = "Почти чисто — осталось закрепить пару мест."
    de_block = "\n".join([
        "📊 ERGEBNIS",
        BAR,
        "Thema: {} ({})".format(topic["title_de"], topic["title"]),
        "Richtig: {} von {} — {}%".format(correct, total, percent),
        "Falsche Töne: {}".format(wrong),
        "",
        de_verdict,
    ])
    ru_block = "\n".join([
        "📊 РЕЗУЛЬТАТ",
        BAR,
        "Тема: {} ({})".format(topic["title"], topic["title_de"]),
        "Верно: {} из {} — {}%".format(correct, total, percent),
        "Фальшивых нот: {}".format(wrong),
        "",
        ru_verdict,
    ])
    text = texts.bi(de_block, ru_block)
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
        "🔄 HANDLUNG NEU STARTEN? / НАЧАТЬ СЮЖЕТ ЗАНОВО?\n"
        "{}\n\n"
        "{}".format(
            BAR,
            texts.bi(
                "Der Barde zerreißt die Rolle und kehrt nach Lübeck zurück: "
                "Die Strophen der Ballade werden zurückgesetzt, die Orte "
                "öffnen sich neu. Die Fehlerhistorie und die Statistik "
                "bleiben — sie helfen beim Training.",
                "Бард порвёт свиток и вернётся в Любек: строфы баллады "
                "сбросятся, локации откроются заново. История ошибок и "
                "статистика сохранятся — они пригодятся в тренировке.",
            ),
        )
    )
    rows = [[texts.BTN_RESTART_YES], [texts.BTN_RESTART_NO]]
    return text, keyboards.build(rows)


def feedback_screen() -> tuple:
    text = (
        "📝 FEEDBACK / ОБРАТНАЯ СВЯЗЬ\n"
        "{}\n\n"
        "{}\n\n"
        "🔗 {}".format(
            BAR,
            texts.bi(
                "Bitte füllt nach dem Durchspielen des Bots den "
                "Feedback-Fragebogen aus. Er hilft, die Regeln, Aufgaben und "
                "die Handlung zu verbessern.",
                "Заполните, пожалуйста, анкету с обратной связью после "
                "прохождения бота. Она поможет улучшить правила, задания и "
                "сюжет.",
            ),
            texts.FEEDBACK_URL,
        )
    )
    rows = [
        [(texts.BTN_OPEN_FORM, texts.FEEDBACK_URL)],
        [texts.BTN_MENU],
    ]
    return text, keyboards.build(rows)


def fallback() -> tuple:
    text = texts.bi(
        "🤔 Das scheint kein Befehl zu sein. Klicke die Schaltflächen unter "
        "der Nachricht — oder wähle, wohin du weitergehen möchtest.",
        "🤔 Похоже, это не команда. Нажимай кнопки под сообщением — "
        "или выбери, куда идти дальше.",
    )
    return text, keyboards.build(
        [[texts.BTN_MENU], [texts.BTN_HELP], [texts.BTN_FEEDBACK]])
