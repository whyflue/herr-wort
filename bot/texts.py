"""Тексты интерфейса: подписи кнопок, разбор команд, нормализация ввода.

Важно: пользовательский longpoll не отдаёт callback-события, поэтому кнопки
у нас обычные текстовые (нажатие = отправка текста кнопки). Вся навигация
сводится к сравнению нормализованного текста сообщения с известными подписями.
"""

import re

# ---------- подписи кнопок ----------
# Навигация подписана на двух языках: сначала немецком, затем русском. Так
# студент видит немецкий эквивалент команды, а бот по-прежнему понимает и
# старые подписи (они перечислены в ALIASES и LEGACY_COMMANDS ниже).

BTN_MENU = "🏠 Menü / Меню"
BTN_HELP = "❓ Hilfe / Помощь"
BTN_STATS = "📊 Statistik / Статистика"
BTN_STORY = "📖 Handlung / Сюжет"
BTN_TRAIN = "🎯 Themen üben / Тренировка по темам"
BTN_NOSTALGIA = "🏰 Orte besuchen / Побывать в местах"
BTN_LISTEN = "🎧 Zuhören / Прислушаться"
BTN_TO_TASKS = "✍️ Zu den Aufgaben / К заданиям"
BTN_SHOW_RULE = "📖 Regel zeigen / Показать правило"
BTN_START_NO_RULE = "✍️ Ohne Regel / Начать без правила"
BTN_NEXT = "➡️ Weiter / Дальше"
BTN_NEXT_LOCATION = "➡️ Nächste Station / Следующая локация"
BTN_FINALE = "🏁 Finale / Финал"
BTN_RETRY_MISTAKES = "🔁 Fehler üben / Отработать ошибки"
BTN_SKIP_RETRY = "➡️ Weitergehen / Продолжить путь"
BTN_RESTART = "🔄 Neu starten / Начать сюжет заново"
BTN_RESTART_YES = "✅ Ja, neu starten / Да, начать заново"
BTN_RESTART_NO = "↩️ Abbrechen / Отмена"
BTN_TO_TOPICS = "🎯 Zur Themenliste / К списку тем"
BTN_TO_PLACES = "🏰 Zu den Orten / К местам"
BTN_AGAIN = "🔄 Wiederholen / Пройти заново"
BTN_CHECK = "✅ Prüfen / Проверить"
BTN_UNDO = "⬅️ Wort entfernen / Убрать слово"
BTN_CLEAR = "🔄 Zurücksetzen / Сбросить"
BTN_FEEDBACK = "📝 Feedback / Обратная связь"
BTN_OPEN_FORM = "📋 Fragebogen öffnen / Открыть анкету"

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
    BTN_FEEDBACK: "feedback",
}


def _reverse_label(label: str) -> str:
    """Меняет местами немецкую и русскую половины подписи «DE / RU».

    Нужно для совместимости: кнопки в уже отправленных сообщениях подписаны
    по-старому («Меню / Menü»), и нажатие на них должно продолжать работать.
    """
    if " / " not in label:
        return ""
    first, second = label.split(" / ", 1)
    prefix, rest = first.split(" ", 1)
    return "{} {} / {}".format(prefix, second, rest)


#: Старые подписи (русский вариант первым) -> ключ команды.
LEGACY_COMMANDS = {}
for _label, _command in COMMANDS.items():
    _old = _reverse_label(_label)
    if _old:
        LEGACY_COMMANDS[_old] = _command

#: Онлайн-анкета обратной связи для кнопки в главном меню.
FEEDBACK_URL = (
    "https://docs.google.com/forms/d/e/"
    "1FAIpQLSccrtF43ttt2AU_5RHNXVlhwqGnH4qOOijC__-Z5N6MMv_l8Q/"
    "viewform?usp=publish-editor"
)

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
    "обратная связь": "feedback",
    "анкета": "feedback",
    "опрос": "feedback",
    "опросник": "feedback",
    "открыть анкету": "feedback",
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
    "feedback": "feedback",
    "rückmeldung": "feedback",
    "rueckmeldung": "feedback",
    "fragebogen": "feedback",
    "fragebogen öffnen": "feedback",
    "fragebogen oeffnen": "feedback",
    "umfrage": "feedback",
}

#: Команды, которые всегда обрабатываются, даже если похожий текст есть
#: среди вариантов ответа текущего задания.
_FORCE = {"menu", "help", "stats", "restart", "restart_no", "feedback"}

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
    for label, command in LEGACY_COMMANDS.items():
        if normalize(label) == key:
            return command
    return ALIASES.get(key, "")


def bi(de: str, ru: str, block: bool = True) -> str:
    """Двуязычный фрагмент: сначала немецкий, затем русский.

    Пустые половины пропускаются, чтобы экран не показывал пустую метку.
    """
    de = (de or "").strip()
    ru = (ru or "").strip()
    if not de:
        return ru
    if not ru:
        return de
    sep = "\n\n" if block else "\n"
    return "🇩🇪 {}{}🇷🇺 {}".format(de, sep, ru)


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
