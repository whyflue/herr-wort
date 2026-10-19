"""Тексты интерфейса: подписи кнопок, разбор команд, нормализация ввода.

Важно: пользовательский longpoll не отдаёт callback-события, поэтому кнопки
у нас обычные текстовые (нажатие = отправка текста кнопки). Вся навигация
сводится к сравнению нормализованного текста сообщения с известными подписями.
"""

import re

# ---------- подписи кнопок ----------
# Навигация подписана на двух языках: русском и немецком. Так студент видит
# немецкий эквивалент команды, а бот по-прежнему понимает и старые подписи
# (они перечислены в ALIASES ниже).

BTN_MENU = "🏠 Меню / Menü"
BTN_HELP = "❓ Помощь / Hilfe"
BTN_STATS = "📊 Статистика / Statistik"
BTN_STORY = "📖 Сюжет / Handlung"
BTN_TRAIN = "🎯 Тренировка по темам / Themen üben"
BTN_NOSTALGIA = "🏰 Побывать в местах / Orte besuchen"
BTN_LISTEN = "🎧 Прислушаться / Zuhören"
BTN_TO_TASKS = "✍️ К заданиям / Zu den Aufgaben"
BTN_SHOW_RULE = "📖 Показать правило / Regel zeigen"
BTN_START_NO_RULE = "✍️ Начать без правила / Ohne Regel"
BTN_NEXT = "➡️ Дальше / Weiter"
BTN_NEXT_LOCATION = "➡️ Следующая локация / Nächste Station"
BTN_FINALE = "🏁 Финал / Finale"
BTN_RETRY_MISTAKES = "🔁 Отработать ошибки / Fehler üben"
BTN_SKIP_RETRY = "➡️ Продолжить путь / Weitergehen"
BTN_RESTART = "🔄 Начать сюжет заново / Neu starten"
BTN_RESTART_YES = "✅ Да, начать заново / Ja, neu starten"
BTN_RESTART_NO = "↩️ Отмена / Abbrechen"
BTN_TO_TOPICS = "🎯 К списку тем / Zur Themenliste"
BTN_TO_PLACES = "🏰 К местам / Zu den Orten"
BTN_AGAIN = "🔄 Пройти заново / Wiederholen"
BTN_CHECK = "✅ Проверить / Prüfen"
BTN_UNDO = "⬅️ Убрать слово / Wort entfernen"
BTN_CLEAR = "🔄 Сбросить / Zurücksetzen"

#: Подписи кнопок-команд: нормализованный текст -> ключ команды.
COMMANDS = {
    BTN_MENU: "menu",
    BTN_HELP: "help",
    BTN_STATS: "stats",
    BTN_STORY: "story",
    BTN_TRAIN: "train",
    BTN_NOSTALGIA: "nostalgia",
    BTN_LISTEN: "listen",
    BTN_TO_TASKS: "to_tasks",
    BTN_SHOW_RULE: "show_rule",
    BTN_START_NO_RULE: "skip_rule",
    BTN_NEXT: "next",
    BTN_NEXT_LOCATION: "next_location",
    BTN_FINALE: "finale",
    BTN_RETRY_MISTAKES: "retry_mistakes",
    BTN_SKIP_RETRY: "skip_retry",
    BTN_RESTART: "restart",
    BTN_RESTART_YES: "restart_yes",
    BTN_RESTART_NO: "restart_no",
    BTN_TO_TOPICS: "to_topics",
    BTN_TO_PLACES: "to_places",
    BTN_AGAIN: "again",
    BTN_CHECK: "check",
    BTN_UNDO: "undo",
    BTN_CLEAR: "clear",
}

#: Дополнительные слова, которые пользователь может набрать руками.
#: Сюда же добавлены старые русские подписи кнопок, чтобы кнопки в уже
#: отправленных сообщениях продолжали работать после перехода на двуязычие.
ALIASES = {
    "начать": "start",
    "start": "start",
    "старт": "start",
    "привет": "start",
    "помоги": "help",
    "меню": "menu",
    "помощь": "help",
    "статистика": "stats",
    "результаты": "stats",
    "сюжет": "story",
    "сюжетный режим": "story",
    "история": "story",
    "тренировка": "train",
    "тренировка по темам": "train",
    "темы": "train",
    "побывать в местах": "nostalgia",
    "прислушаться": "listen",
    "к заданиям": "to_tasks",
    "правило": "show_rule",
    "показать правило": "show_rule",
    "без правила": "skip_rule",
    "начать без правила": "skip_rule",
    "дальше": "next",
    "следующая локация": "next_location",
    "финал": "finale",
    "отработать сложные места": "retry_mistakes",
    "отработать ошибки": "retry_mistakes",
    "продолжить путь": "skip_retry",
    "начать сюжет заново": "restart",
    "да начать заново": "restart_yes",
    "отмена": "restart_no",
    "к списку тем": "to_topics",
    "к местам": "to_places",
    "пройти тему заново": "again",
    "пройти заново": "again",
    "проверить": "check",
    "убрать слово": "undo",
    "сбросить": "clear",
    # немецкие команды: можно набрать вручную, без кнопок
    "menü": "menu",
    "menue": "menu",
    "hilfe": "help",
    "statistik": "stats",
    "handlung": "story",
    "geschichte": "story",
    "themen üben": "train",
    "themen ueben": "train",
    "training": "train",
    "orte besuchen": "nostalgia",
    "zuhören": "listen",
    "zuhoeren": "listen",
    "zu den aufgaben": "to_tasks",
    "regel zeigen": "show_rule",
    "ohne regel": "skip_rule",
    "weiter": "next",
    "nächste station": "next_location",
    "naechste station": "next_location",
    "finale": "finale",
    "fehler üben": "retry_mistakes",
    "fehler ueben": "retry_mistakes",
    "weitergehen": "skip_retry",
    "neu starten": "restart",
    "ja neu starten": "restart_yes",
    "abbrechen": "restart_no",
    "zur themenliste": "to_topics",
    "zu den orten": "to_places",
    "wiederholen": "again",
    "prüfen": "check",
    "pruefen": "check",
    "wort entfernen": "undo",
    "zurücksetzen": "clear",
    "zuruecksetzen": "clear",
}

#: Команды, которые всегда обрабатываются, даже если похожий текст есть
#: среди вариантов ответа текущего задания.
_FORCE = {"menu", "help", "stats", "restart", "restart_no"}

_EMOJI_RE = re.compile(
    "[\U0001F000-\U0001FAFF\u2190-\u21FF\u2600-\u27BF\uFE0F\u2B00-\u2BFF]"
)
_EXTRA_RE = re.compile(r"[^\w\s]+", re.UNICODE)


def normalize(text: str) -> str:
    """Приводит текст к сравнимому виду: без эмодзи, пунктуации и регистра."""
    text = (text or "").replace("ё", "е").replace("Ё", "Е")
    text = _EMOJI_RE.sub(" ", text)
    text = _EXTRA_RE.sub(" ", text)
    return " ".join(text.lower().split())


def resolve(text: str) -> str:
    """Возвращает ключ команды для введённого текста или пустую строку."""
    key = normalize(text)
    if not key:
        return ""
    for label, command in COMMANDS.items():
        if normalize(label) == key:
            return command
    return ALIASES.get(key, "")


_ANSWER_FOLD = str.maketrans({
    "ä": "ae",
    "ö": "oe",
    "ü": "ue",
    "ß": "ss",
})


def normalize_answer(text: str) -> str:
    """Нормализация свободного ответа: без регистра, пунктуации и умлаутов.

    Немецкие буквы ä/ö/ü/ß сравниваются и в обычном написании, и в замене
    на ae/oe/ue/ss, чтобы ответ можно было набрать без немецкой раскладки.
    """
    return normalize(text).translate(_ANSWER_FOLD)


def answers_match(given: str, expected: str) -> bool:
    return normalize_answer(given) == normalize_answer(expected)


def is_forced(command: str) -> bool:
    return command in _FORCE


def command_labels() -> set:
    """Нормализованные подписи команд — для валидации контента."""
    return {normalize(label) for label in COMMANDS} | set(ALIASES)
