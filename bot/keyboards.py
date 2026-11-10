"""Сборка клавиатур VK.

Ограничения платформы: не больше 40 символов в подписи кнопки, не больше
5 кнопок в ряду и не больше 10 рядов. Используем только текстовые кнопки,
потому что у пользовательского токена callback-события не приходят.
"""

import json

MAX_LABEL = 40
MAX_ROWS = 10
MAX_PER_ROW = 5


class KeyboardError(ValueError):
    """Клавиатура нарушает ограничения VK."""


def _button(item) -> dict:
    """Кнопка-текст из строки или кнопка-ссылка из пары (подпись, URL)."""
    link = None
    if isinstance(item, (tuple, list)):
        if len(item) != 2:
            raise KeyboardError("Кнопка-ссылка задаётся парой (подпись, URL)")
        label, link = item
    else:
        label = item
    label = str(label).strip()
    if not label:
        raise KeyboardError("Пустая подпись кнопки")
    if len(label) > MAX_LABEL:
        raise KeyboardError(f"Слишком длинная подпись ({len(label)}): {label!r}")
    if link is not None:
        link = str(link).strip()
        if not link:
            raise KeyboardError("Пустая ссылка кнопки")
        return {"action": {"type": "open_link", "link": link, "label": label}}
    return {"action": {"type": "text", "label": label}}


def build(rows: list) -> dict:
    """rows: список рядов; элемент ряда — подпись или пара (подпись, URL)."""
    rows = [row for row in rows if row]
    if len(rows) > MAX_ROWS:
        raise KeyboardError(f"Слишком много рядов: {len(rows)}")
    for row in rows:
        if len(row) > MAX_PER_ROW:
            raise KeyboardError(f"Слишком много кнопок в ряду: {len(row)}")
    return {
        "one_time": False,
        "inline": False,
        "buttons": [[_button(label) for label in row] for row in rows],
    }


def dumps(keyboard: dict) -> str:
    return json.dumps(keyboard, ensure_ascii=False)


def pack(labels: list, per_row: int = 5, max_width: int = 34) -> list:
    """Раскладывает подписи по рядам, не превышая ширину ряда.

    Нужно для заданий, где кнопками служат слова предложения: они бывают
    длинными, и 5 таких кнопок в ряд не помещаются.
    """
    rows, current, width = [], [], 0
    for label in labels:
        length = len(label) + 1
        if current and (len(current) >= per_row or width + length > max_width):
            rows.append(current)
            current, width = [], 0
        current.append(label)
        width += length
    if current:
        rows.append(current)
    return rows


def single_row_options(labels: list) -> list:
    """Варианты ответа: по одному-два в ряд в зависимости от длины."""
    wide = any(len(label) > 16 for label in labels)
    per_row = 1 if wide else 2
    return [labels[i:i + per_row] for i in range(0, len(labels), per_row)]
