"""Проверка банка грамматических материалов: схема, кнопки, однозначность.

Запуск:  python check_content.py
Выход 1, если найдены проблемы (удобно для CI и для авторов контента).
"""

import sys

import content
from bot import texts, keyboards

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def print_overview() -> None:
    print("Банк материалов: {}".format(content.summary()))
    for topic in content.TOPICS:
        exercises = topic["exercises"]
        retries = sum(1 for ex in exercises if ex.get("retry"))
        print("  {nr:>2}. {short:<30} {loc:<32} заданий: {n} (с отработкой: {r})".format(
            nr=topic["nr"],
            short=topic["short"],
            loc=topic["location"],
            n=len(exercises),
            r=retries,
        ))


def _keyboard_problems() -> list:
    """Проверяет, что все клавиатуры, которые построит бот, влезают в лимиты."""
    problems = []
    for topic in content.TOPICS:
        for exercise in topic["exercises"]:
            for is_retry in (False, True):
                if is_retry and not exercise.get("retry"):
                    continue
                variant = content.variant(exercise, is_retry)
                try:
                    build_keyboard(variant)
                except keyboards.KeyboardError as exc:
                    problems.append("{}: {}".format(variant["id"], exc))
    return problems


def build_keyboard(exercise: dict) -> dict:
    """Собирает клавиатуру задания так же, как это делает движок бота."""
    mechanics = content.kind_mechanics(exercise["kind"])
    if mechanics == "choice":
        rows = keyboards.single_row_options(exercise["options"])
        rows.append([texts.BTN_MENU])
        return keyboards.build(rows)
    if mechanics == "order":
        rows = keyboards.pack(exercise["words"], per_row=3)
        rows.append([texts.BTN_UNDO, texts.BTN_CLEAR, texts.BTN_CHECK])
        rows.append([texts.BTN_MENU])
        return keyboards.build(rows)
    words = exercise["sentence"].split()
    rows = keyboards.pack(words, per_row=3)
    rows.append([texts.BTN_MENU])
    return keyboards.build(rows)


def main() -> int:
    print_overview()
    problems = content.validate() + _keyboard_problems()
    print()
    if not problems:
        print("Проверки пройдены: проблем не найдено.")
        return 0
    print("Найдено проблем: {}".format(len(problems)))
    for problem in problems:
        print("  - {}".format(problem))
    return 1


if __name__ == "__main__":
    sys.exit(main())
