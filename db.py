"""Хранение состояния диалога и прогресса пользователя (SQLite)."""

import json
import sqlite3
import threading
import time


def _now() -> int:
    return int(time.time())


class Database:
    def __init__(self, path: str):
        self.path = path
        self._lock = threading.Lock()
        self._conn = sqlite3.connect(path, check_same_thread=False)
        self._conn.row_factory = sqlite3.Row
        self._init_schema()

    def _init_schema(self) -> None:
        with self._lock, self._conn:
            self._conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS users (
                    vk_id      INTEGER PRIMARY KEY,
                    state      TEXT NOT NULL DEFAULT '{}',
                    created_at INTEGER NOT NULL,
                    updated_at INTEGER NOT NULL
                );

                CREATE TABLE IF NOT EXISTS progress (
                    vk_id    INTEGER NOT NULL,
                    topic_id TEXT NOT NULL,
                    status   TEXT NOT NULL DEFAULT 'done',
                    done_at  INTEGER NOT NULL,
                    PRIMARY KEY (vk_id, topic_id)
                );

                CREATE TABLE IF NOT EXISTS mistakes (
                    vk_id       INTEGER NOT NULL,
                    ex_id       TEXT NOT NULL,
                    topic_id    TEXT NOT NULL,
                    wrong_count INTEGER NOT NULL DEFAULT 1,
                    resolved    INTEGER NOT NULL DEFAULT 0,
                    last_at     INTEGER NOT NULL,
                    PRIMARY KEY (vk_id, ex_id)
                );

                CREATE TABLE IF NOT EXISTS attempts (
                    id        INTEGER PRIMARY KEY AUTOINCREMENT,
                    vk_id     INTEGER NOT NULL,
                    topic_id  TEXT NOT NULL,
                    kind      TEXT NOT NULL,
                    correct   INTEGER NOT NULL,
                    wrong     INTEGER NOT NULL,
                    finished_at INTEGER NOT NULL
                );
                """
            )

    # ---------- состояние диалога ----------

    def get_state(self, vk_id: int) -> dict:
        with self._lock:
            row = self._conn.execute(
                "SELECT state FROM users WHERE vk_id = ?", (vk_id,)
            ).fetchone()
        if not row:
            return {}
        try:
            return json.loads(row["state"])
        except (TypeError, ValueError):
            return {}

    def set_state(self, vk_id: int, state: dict) -> None:
        payload = json.dumps(state, ensure_ascii=False)
        with self._lock, self._conn:
            self._conn.execute(
                """
                INSERT INTO users (vk_id, state, created_at, updated_at)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(vk_id) DO UPDATE SET state = excluded.state,
                                                 updated_at = excluded.updated_at
                """,
                (vk_id, payload, _now(), _now()),
            )

    # ---------- прогресс сюжета ----------

    def mark_topic_done(self, vk_id: int, topic_id: str) -> None:
        with self._lock, self._conn:
            self._conn.execute(
                """
                INSERT INTO progress (vk_id, topic_id, status, done_at)
                VALUES (?, ?, 'done', ?)
                ON CONFLICT(vk_id, topic_id) DO UPDATE SET done_at = excluded.done_at
                """,
                (vk_id, topic_id, _now()),
            )

    def done_topics(self, vk_id: int) -> list:
        with self._lock:
            rows = self._conn.execute(
                "SELECT topic_id FROM progress WHERE vk_id = ? ORDER BY done_at",
                (vk_id,),
            ).fetchall()
        return [r["topic_id"] for r in rows]

    def reset_story(self, vk_id: int) -> None:
        """Начать сюжет заново: собранные строки песни и отметки локаций стираются,
        история попыток и статистика ошибок сохраняются."""
        with self._lock, self._conn:
            self._conn.execute("DELETE FROM progress WHERE vk_id = ?", (vk_id,))

    def all_users(self) -> list:
        """Идентификаторы всех, кто писал боту (для отчёта по апробации)."""
        with self._lock:
            rows = self._conn.execute(
                "SELECT vk_id FROM users ORDER BY created_at"
            ).fetchall()
        return [r["vk_id"] for r in rows]

    # ---------- ошибки ----------

    def log_mistake(self, vk_id: int, topic_id: str, ex_id: str) -> None:
        with self._lock, self._conn:
            self._conn.execute(
                """
                INSERT INTO mistakes (vk_id, ex_id, topic_id, wrong_count, resolved, last_at)
                VALUES (?, ?, ?, 1, 0, ?)
                ON CONFLICT(vk_id, ex_id) DO UPDATE SET
                    wrong_count = wrong_count + 1,
                    resolved = 0,
                    last_at = excluded.last_at
                """,
                (vk_id, ex_id, topic_id, _now()),
            )

    def resolve_mistake(self, vk_id: int, ex_id: str) -> None:
        with self._lock, self._conn:
            self._conn.execute(
                "UPDATE mistakes SET resolved = 1 WHERE vk_id = ? AND ex_id = ?",
                (vk_id, ex_id),
            )

    def topic_mistakes(self, vk_id: int, topic_id: str) -> list:
        with self._lock:
            rows = self._conn.execute(
                """
                SELECT ex_id, wrong_count, resolved FROM mistakes
                WHERE vk_id = ? AND topic_id = ? ORDER BY last_at
                """,
                (vk_id, topic_id),
            ).fetchall()
        return [dict(r) for r in rows]

    # ---------- результаты ----------

    def save_attempt(self, vk_id: int, topic_id: str, kind: str,
                     correct: int, wrong: int) -> None:
        with self._lock, self._conn:
            self._conn.execute(
                """
                INSERT INTO attempts (vk_id, topic_id, kind, correct, wrong, finished_at)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (vk_id, topic_id, kind, correct, wrong, _now()),
            )

    def topic_results(self, vk_id: int, topic_id: str) -> dict:
        """Сводка по теме: лучший результат и общие цифры."""
        with self._lock:
            rows = self._conn.execute(
                """
                SELECT correct, wrong FROM attempts
                WHERE vk_id = ? AND topic_id = ? ORDER BY finished_at
                """,
                (vk_id, topic_id),
            ).fetchall()
        if not rows:
            return {"attempts": 0, "best": None, "correct": 0, "wrong": 0}
        total_c = sum(r["correct"] for r in rows)
        total_w = sum(r["wrong"] for r in rows)
        best = max(
            (r["correct"] / (r["correct"] + r["wrong"]) for r in rows
             if r["correct"] + r["wrong"]),
            default=0.0,
        )
        return {
            "attempts": len(rows),
            "best": round(best * 100),
            "correct": total_c,
            "wrong": total_w,
        }

    def overall_stats(self, vk_id: int) -> dict:
        with self._lock:
            row = self._conn.execute(
                """
                SELECT COALESCE(SUM(correct), 0) AS c, COALESCE(SUM(wrong), 0) AS w,
                       COUNT(*) AS n FROM attempts WHERE vk_id = ?
                """,
                (vk_id,),
            ).fetchone()
            unresolved = self._conn.execute(
                "SELECT COUNT(*) AS n FROM mistakes WHERE vk_id = ? AND resolved = 0",
                (vk_id,),
            ).fetchone()
        total = row["c"] + row["w"]
        return {
            "attempts": row["n"],
            "correct": row["c"],
            "wrong": row["w"],
            "accuracy": round(row["c"] / total * 100) if total else 0,
            "unresolved": unresolved["n"],
        }

    def close(self) -> None:
        with self._lock:
            self._conn.close()
