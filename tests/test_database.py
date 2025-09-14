import sqlite3
from datetime import datetime
from pathlib import Path

import pytest
from cli_todo import database
from cli_todo.models import Task

TEST_DB = Path(__file__).parent / "test_tasks.db"


@pytest.fixture
def setup_test_db():
    database.DB_PATH = TEST_DB
    database.init_db()

    yield

    if TEST_DB.exists():
        TEST_DB.unlink()


def test_save_and_get_task(setup_test_db):
    task = Task(
        id=None,
        title="Test Task",
        description="Test Description",
        due_date=datetime.now(),
    )
    database.save_task(task)

    tasks = database.get_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "Test Task"
    assert tasks[0].id is not None


def test_complete_task(setup_test_db):
    task = Task(id=None, title="Do Work")
    database.save_task(task)
    database.complete_task(task.id)

    t = database.get_tasks()[0]
    assert t.completed == True


def test_delete_task(setup_test_db):
    task = Task(id=None, title="Delete Me")
    database.save_task(task)

    database.delete_task(task.id)
    tasks = database.get_tasks()
    assert len(tasks) == 0
