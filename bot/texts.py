"""Тексты интерфейса: подписи кнопок, разбор команд, нормализация ввода.

Важно: пользовательский longpoll не отдаёт callback-события, поэтому кнопки
у нас обычные текстовые (нажатие = отправка текста кнопки). Вся навигация
сводится к сравнению нормализованного текста сообщения с известными подписями.
"""

import re

# ---------- подписи кнопок ----------

BTN_MENU = "🏠 Меню"
BTN_HELP = "❓ Помощь"
BTN_STATS = "📊 Статистика"
BTN_STORY = "📖 Сюжет"
BTN_TRAIN = "🎯 Тренировка по темам"
BTN_NOSTALGIA = "🏰 Побывать в местах"
BTN_LISTEN = "🎧 Прислушаться"
BTN_TO_TASKS = "✍️ К заданиям"
BTN_NEXT = "➡️ Дальше"
BTN_NEXT_LOCATION = "➡️ Следующая локация"
BTN_FINALE = "🏁 Финал"
BTN_RETRY_MISTAKES = "🔁 Отработать сложные места"
BTN_SKIP_RETRY = "➡️ Продолжить путь"
BTN_RESTART = "🔄 Начать сюжет заново"
BTN_RESTART_YES = "✅ Да, начать заново"
BTN_RESTART_NO = "↩️ Отмена"
BTN_TO_TOPICS = "🎯 К списку тем"
BTN_TO_PLACES = "🏰 К местам"
BTN_AGAIN = "🔄 Пройти тему заново"
BTN_CHECK = "✅ Проверить"
BTN_UNDO = "⬅️ Убрать слово"
BTN_CLEAR = "🔄 Сбросить"

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
ALIASES = {
    "начать": "start",
    "start": "start",
    "старт": "start",
    "привет": "start",
    "помоги": "help",
    "сюжетный режим": "story",
    "история": "story",
    "тренировка": "train",
    "темы": "train",
    "статистика": "stats",
    "результаты": "stats",
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


def is_forced(command: str) -> bool:
    return command in _FORCE


def command_labels() -> set:
    """Нормализованные подписи команд — для валидации контента."""
    return {normalize(label) for label in COMMANDS} | set(ALIASES)
