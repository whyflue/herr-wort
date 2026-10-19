"""Сводка результатов по всем игрокам: для апробации и разбора после неё.

    python stats.py                 # таблица по пользователям, которые играли
    python stats.py --csv report.csv  # выгрузить таблицу в CSV (Excel)
    python stats.py --user 123456     # подробно по одному игроку
"""

import argparse
import csv
import sys
from pathlib import Path

import config
import content
from db import Database

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BAR = "─" * 60


def users(db: Database) -> list:
    return db.all_users()


def overview(db: Database) -> list:
    data = []
    for vk_id in users(db):
        stats = db.overall_stats(vk_id)
        done = db.done_topics(vk_id)
        data.append({
            "vk_id": vk_id,
            "locations": len(done),
            "attempts": stats["attempts"],
            "correct": stats["correct"],
            "wrong": stats["wrong"],
            "accuracy": stats["accuracy"],
            "unresolved": stats["unresolved"],
        })
    return data


def print_overview(data: list) -> None:
    print("Сводка по игрокам (всего: {})".format(len(data)))
    print(BAR)
    header = "{:<12} {:>9} {:>8} {:>8} {:>7} {:>9} {:>10}".format(
        "vk_id", "локаций", "попыток", "верно", "ошибок", "точность", "незакрыто")
    print(header)
    for row in data:
        print("{vk_id:<12} {locations:>9} {attempts:>8} {correct:>8} "
              "{wrong:>7} {accuracy:>8}% {unresolved:>10}".format(**row))
    if not data:
        print("Пока никто не играл: база пуста.")


def print_user(db: Database, vk_id: int) -> None:
    print("Игрок {}".format(vk_id))
    print(BAR)
    stats = db.overall_stats(vk_id)
    done = db.done_topics(vk_id)
    print("Локаций пройдено: {} из {}".format(len(done), len(content.TOPICS)))
    print("Решено: {}, ошибок: {}, точность: {}%".format(
        stats["correct"], stats["wrong"], stats["accuracy"]))
    print("Незакрытых ошибок: {}".format(stats["unresolved"]))
    print()
    for topic in content.TOPICS:
        result = db.topic_results(vk_id, topic["id"])
        mistakes = [m for m in db.topic_mistakes(vk_id, topic["id"]) if not m["resolved"]]
        mark = "✅" if topic["id"] in done else "·"
        best = "—" if result["best"] is None else "{}%".format(result["best"])
        print("{} {}. {:<26} лучший: {:<5} попыток: {:<3} незакрытых ошибок: {}".format(
            mark, topic["nr"], topic["short"], best, result["attempts"], len(mistakes)))


def export_csv(data: list, path: str) -> None:
    with open(path, "w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=[
            "vk_id", "locations", "attempts", "correct", "wrong", "accuracy", "unresolved"])
        writer.writeheader()
        writer.writerows(data)
    print("Таблица сохранена: {}".format(Path(path).resolve()))


def main() -> int:
    parser = argparse.ArgumentParser(description="Результаты игроков бота «Бард»")
    parser.add_argument("--db", default=None, help="файл базы (по умолчанию из .env)")
    parser.add_argument("--csv", default=None, help="выгрузить сводку в CSV")
    parser.add_argument("--user", type=int, default=None, help="подробно по игроку")
    args = parser.parse_args()

    db = Database(args.db or config.DB_PATH)
    try:
        if args.user:
            print_user(db, args.user)
            return 0
        data = overview(db)
        print_overview(data)
        if args.csv:
            export_csv(data, args.csv)
    finally:
        db.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
