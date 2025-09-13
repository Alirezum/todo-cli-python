import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Optional

from models import Task

DB_PATH = Path(__file__).parent / "tasks.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                due_date TEXT,
                completed INTEGER DEFAULT 0
            )
        """
        )


def _row_to_task(row: sqlite3.Row) -> Task:
    due_date = datetime.fromisoformat(row["due_date"]) if row["due_date"] else None
    completed = bool(row["completed"])
    return Task(
        id=row["id"],
        title=row["title"],
        description=row["description"] or "",
        due_date=due_date,
        completed=completed,
    )


def save_task(task: Task) -> Task:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO tasks (title, description, due_date, completed) VALUES (?, ?, ?, ?)",
            (
                task.title,
                task.description,
                task.due_date.isoformat() if task.due_date else None,
                int(task.completed),
            ),
        )
        task.id = cur.lastrowid
    return task


def get_tasks() -> list[Task]:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks ORDER BY id")
        rows = cur.fetchall()
    return [_row_to_task(row) for row in rows]


def complete_task(task_id: int) -> bool:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        return cur.rowcount > 0


def delete_task(task_id: int) -> bool:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        return cur.rowcount > 0
