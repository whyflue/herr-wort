"""Банк грамматических материалов: 12 тем A1–A2 для чат-бота «Бард».

Каждая тема — отдельный модуль в пакете `content.topics` с словарём TOPIC.
Материалы двуязычны, как в exercises.txt: у каждой страницы правила есть
русский (`body`) и немецкий (`body_de`) текст, у каждого задания — русское
(`explain`) и немецкое (`explain_de`) объяснение.
Здесь темы собираются в единый список, к ним добавлены утилиты поиска и
валидатор schema (см. `content/SCHEMA.md` и `check_content.py`).
"""

import importlib
from pathlib import Path

from bot import texts

TOPICS_DIR = Path(__file__).parent / "topics"

#: Заголовок и зачин баллады, которую пишет бард по мере прохождения сюжета.
BALLAD_TITLE = "Баллада о барде, который учил немецкий"
BALLAD_INTRO = (
    "Запев: «Я пел о том, чего не знал, — и вот перо беру…»"
)

#: Виды заданий. Механика проверки: choice — выбор варианта, input — свободный
#: ввод, order — сборка предложения из слов, error — поиск ошибки в предложении.
KINDS = {
    "mc": "choice",
    "gap": "input",
    "input": "input",
    "join": "choice",
    "transform": "choice",
    "translate": "choice",
    "order": "order",
    "error": "error",
}

KIND_TITLES = {
    "mc": "Выбери правильный вариант",
    "gap": "Заполни пропуск",
    "input": "Напиши ответ",
    "join": "Соедини два предложения в одно",
    "transform": "Преобразуй предложение",
    "translate": "Переведи фрагмент на немецкий",
    "order": "Собери предложение из слов",
    "error": "Найди ошибку в предложении",
}

_KIND_HINTS = {
    "mc": "нажми на правильный вариант",
    "gap": "напиши пропущенное слово или форму сообщением",
    "input": "напиши ответ сообщением",
    "join": "нажми на правильный вариант",
    "transform": "нажми на правильный вариант",
    "translate": "нажми на правильный вариант",
    "order": "нажимай на слова по порядку, затем «Проверить»",
    "error": "нажми на слово, в котором ошибка",
}


def _load_topics() -> list:
    topics = []
    for path in sorted(TOPICS_DIR.glob("t*.py")):
        if path.name.startswith("_"):
            continue
        module = importlib.import_module(
            "{}.topics.{}".format(__package__, path.stem)
        )
        topic = getattr(module, "TOPIC", None)
        if not isinstance(topic, dict):
            raise ValueError("В модуле {} нет словаря TOPIC".format(path.name))
        topics.append(topic)
    topics.sort(key=lambda item: item["nr"])
    return topics


TOPICS = _load_topics()
TOPICS_BY_ID = {topic["id"]: topic for topic in TOPICS}


def get_topic(topic_id: str) -> dict:
    return TOPICS_BY_ID[topic_id]


def find_exercise(topic: dict, ex_id: str) -> dict:
    for exercise in topic["exercises"]:
        if exercise["id"] == ex_id:
            return exercise
    raise KeyError("Нет задания {} в теме {}".format(ex_id, topic["id"]))


def kind_mechanics(kind: str) -> str:
    return KINDS[kind]


def kind_title(kind: str) -> str:
    return KIND_TITLES[kind]


def kind_hint(kind: str) -> str:
    return _KIND_HINTS[kind]


def variant(exercise: dict, retry: bool) -> dict:
    """Возвращает задание для показа: исходное или «похожее» (поле retry)."""
    if not retry or not exercise.get("retry"):
        return exercise
    merged = dict(exercise["retry"])
    merged.setdefault("kind", exercise["kind"])
    merged["id"] = exercise["id"]
    merged["retry_of"] = exercise["id"]
    # Двуязычность сохраняется и в отработке: если в retry нет prompt или
    # объяснений, берём их у исходного задания.
    for field in ("prompt", "explain", "explain_de"):
        if not merged.get(field) and exercise.get(field):
            merged[field] = exercise[field]
    return merged


def wrong_words(exercise: dict) -> list:
    """Слова с ошибкой в задании kind=error (одно слово или их список)."""
    wrong = exercise.get("wrong")
    if isinstance(wrong, list):
        return [word for word in wrong if isinstance(word, str)]
    return [wrong] if isinstance(wrong, str) else []


def accepted_answers(exercise: dict) -> list:
    """Все допустимые свободные ответы задания (answers или answer)."""
    answers = exercise.get("answers")
    if isinstance(answers, list) and answers:
        return [answer for answer in answers if isinstance(answer, str)]
    answer = exercise.get("answer")
    return [answer] if isinstance(answer, str) else []


# ---------- валидация ----------


def _check_choice(exercise: dict, where: str, problems: list) -> None:
    options = exercise.get("options")
    if not isinstance(options, list) or not 2 <= len(options) <= 5:
        problems.append("{}: options должны содержать 2–5 вариантов".format(where))
        return
    seen = set()
    for option in options:
        if not isinstance(option, str) or not option.strip():
            problems.append("{}: пустой вариант ответа".format(where))
            continue
        if len(option) > 40:
            problems.append("{}: вариант длиннее 40 символов: {!r}".format(where, option))
        key = texts.normalize(option)
        if key in seen:
            problems.append("{}: повторяющийся вариант {!r}".format(where, option))
        seen.add(key)
        if key in texts.command_labels():
            problems.append("{}: вариант совпадает с командой: {!r}".format(where, option))
    answer = exercise.get("answer")
    if not isinstance(answer, int) or not 0 <= answer < len(options):
        problems.append("{}: answer вне диапазона вариантов".format(where))


def _check_input(exercise: dict, where: str, problems: list) -> None:
    answers = exercise.get("answers")
    if answers is None:
        answer = exercise.get("answer")
        answers = [answer] if isinstance(answer, str) else []
    if not isinstance(answers, list) or not answers:
        problems.append("{}: нужен непустой answer или answers".format(where))
        return
    seen = set()
    for answer in answers:
        if not isinstance(answer, str) or not answer.strip():
            problems.append("{}: пустой вариант свободного ответа".format(where))
            continue
        key = texts.normalize_answer(answer)
        if key in seen:
            problems.append("{}: повторяющийся ответ {!r}".format(where, answer))
        seen.add(key)
        if key in texts.command_labels():
            problems.append("{}: ответ совпадает с командой: {!r}".format(where, answer))


def _check_order(exercise: dict, where: str, problems: list) -> None:
    words = exercise.get("words")
    if not isinstance(words, list) or not 3 <= len(words) <= 12:
        problems.append("{}: words должны содержать 3–12 слов".format(where))
        return
    for word in words:
        if not isinstance(word, str) or not word.strip():
            problems.append("{}: пустое слово".format(where))
        elif len(word) > 40:
            problems.append("{}: слово длиннее 40 символов: {!r}".format(where, word))
        elif texts.normalize(word) in texts.command_labels():
            problems.append("{}: слово совпадает с командой: {!r}".format(where, word))
    answer = exercise.get("answer")
    if isinstance(answer, str) and answer.strip():
        expected = texts.normalize(" ".join(words))
        if texts.normalize(answer) != expected:
            problems.append("{}: answer не совпадает с порядком слов".format(where))


def _check_error(exercise: dict, where: str, problems: list) -> None:
    sentence = exercise.get("sentence", "")
    wrong = exercise.get("wrong", "")
    if not isinstance(sentence, str) or len(sentence.split()) < 3:
        problems.append("{}: sentence слишком короткое".format(where))
        return
    wrong_words = wrong if isinstance(wrong, list) else [wrong]
    if not wrong_words or not all(isinstance(word, str) and word.strip()
                                  for word in wrong_words):
        problems.append("{}: не указано слово с ошибкой".format(where))
    else:
        sentence_words = [texts.normalize(w) for w in sentence.split()]
        for word in wrong_words:
            if texts.normalize(word) not in sentence_words:
                problems.append(
                    "{}: слово с ошибкой {!r} отсутствует в предложении".format(
                        where, word)
                )
    solution = exercise.get("solution")
    if solution is not None and not isinstance(solution, str):
        problems.append("{}: solution должен быть строкой".format(where))
    fix = exercise.get("fix")
    if fix is not None:
        _check_choice(fix, where + "/fix", problems)


def _check_exercise(exercise: dict, topic_id: str, where: str, problems: list) -> None:
    kind = exercise.get("kind")
    if kind not in KINDS:
        problems.append("{}: неизвестный вид задания {!r}".format(where, kind))
        return
    if not isinstance(exercise.get("prompt"), str) or not exercise["prompt"].strip():
        problems.append("{}: пустой prompt".format(where))
    if not isinstance(exercise.get("explain"), str) or not exercise["explain"].strip():
        problems.append("{}: пустое explain".format(where))
    if not isinstance(exercise.get("explain_de"), str) or not exercise["explain_de"].strip():
        problems.append(
            "{}: пустое explain_de (как в exercises.txt, объяснение нужно "
            "на двух языках)".format(where))
    mechanics = KINDS[kind]
    if mechanics == "choice":
        _check_choice(exercise, where, problems)
    elif mechanics == "input":
        _check_input(exercise, where, problems)
    elif mechanics == "order":
        _check_order(exercise, where, problems)
    else:
        _check_error(exercise, where, problems)
    retry = exercise.get("retry")
    if retry is not None:
        clone = dict(retry)
        clone.setdefault("kind", kind)
        clone.setdefault("explain", exercise.get("explain", ""))
        clone.setdefault("explain_de", exercise.get("explain_de", ""))
        clone.setdefault("prompt", exercise.get("prompt", ""))
        _check_exercise(clone, topic_id, where + "/retry", problems)


def validate() -> list:
    """Проверяет весь банк материалов и возвращает список проблем."""
    problems = []
    seen_ids, seen_nrs = set(), set()
    for topic in TOPICS:
        required = (
            "id", "nr", "title", "short", "short_de", "title_de", "location",
            "location_de", "intro", "listen", "theory", "song_line", "exercises",
        )
        for field in required:
            if not topic.get(field):
                problems.append("Тема {}: не заполнено поле {}".format(
                    topic.get("id", "?"), field))
        if topic.get("nr") in seen_nrs:
            problems.append("Тема {}: номер {} повторяется".format(
                topic.get("id"), topic.get("nr")))
        seen_nrs.add(topic.get("nr"))
        if topic["id"] in seen_ids:
            problems.append("Тема {}: id повторяется".format(topic["id"]))
        seen_ids.add(topic["id"])
        if len(topic.get("short", "")) > 30:
            problems.append("Тема {}: short длиннее 30 символов".format(topic["id"]))
        if len(topic.get("short_de", "")) > 30:
            problems.append("Тема {}: short_de длиннее 30 символов".format(topic["id"]))
        theory = topic.get("theory") or []
        if not theory:
            problems.append("Тема {}: нет страниц теории".format(topic["id"]))
        for page in theory:
            body = (page or {}).get("body", "")
            if len(body) > 900:
                problems.append("Тема {}: страница теории длиннее 900 символов: {}".format(
                    topic["id"], page.get("title")))
            body_de = (page or {}).get("body_de", "")
            if not body_de.strip():
                problems.append(
                    "Тема {}: у страницы {!r} нет немецкого текста body_de".format(
                        topic["id"], page.get("title")))
            elif len(body_de) > 900:
                problems.append(
                    "Тема {}: немецкая страница теории длиннее 900 символов: {}".format(
                        topic["id"], page.get("title")))
        exercises = topic.get("exercises") or []
        if len(exercises) < 5:
            problems.append("Тема {}: меньше 5 заданий".format(topic["id"]))
        for exercise in exercises:
            ex_id = exercise.get("id", "")
            prefix = topic["id"] + "_"
            if not ex_id.startswith(prefix):
                problems.append("Задание {}: id должен начинаться с {}".format(ex_id, prefix))
            if ex_id in seen_ids:
                problems.append("Задание {}: id повторяется".format(ex_id))
            seen_ids.add(ex_id)
            _check_exercise(exercise, topic["id"], ex_id, problems)
    return problems


def summary() -> str:
    """Короткая сводка банка материалов для README и проверок."""
    exercises = sum(len(topic["exercises"]) for topic in TOPICS)
    return "тем: {}, заданий: {}".format(len(TOPICS), exercises)
