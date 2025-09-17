from datetime import datetime

import typer
from tabulate2 import tabulate

from cli_todo import database
from cli_todo.models import Task

app = typer.Typer()


@app.command()
def add(
    title: str = typer.Option(..., prompt="Task Title"),
    description: str = typer.Option(..., prompt="Task Description"),
    due_date: str = typer.Option("", prompt="Due Date (YYYY-MM-DD) optional"),
):
    if due_date:
        due = datetime.fromisoformat(due_date)
    else:
        due = None

    task = Task(id=None, title=title, description=description, due_date=due)
    saved_task = database.save_task(task)
    typer.echo(f"Task Added! ID: {saved_task.id}")


@app.command()
def list_tasks():
    tasks = database.get_tasks()
    if not tasks:
        typer.echo("No tasks found!")
        return

    table_data = []
    for task in tasks:
        due_date_str = task.due_date.strftime("%Y-%m-%d") if task.due_date else "-"
        table_data.append(
            [
                task.id,
                task.title,
                "done" if task.completed else "pending",
                due_date_str,
                task.description,
            ]
        )
    headers = {"ID": 1, "Title": 2, "status": 3, "Due Date": 4, "Description": 5}
    typer.echo(tabulate(table_data, headers=headers, tablefmt="rounded_outline"))


@app.command()
def complete(task_id: int):
    success = database.complete_task(task_id)
    if success:
        typer.echo(f"Task {task_id} Marked as Complete")
    else:
        typer.echo(f"Task {task_id} Not Found!")


@app.command()
def delete(task_id: int):
    success = database.delete_task(task_id)
    if success:
        typer.echo(f"Task {task_id} Deleted!")
    else:
        typer.echo(f"Task {task_id} Not Found!")


if __name__ == "__main__":
    database.init_db()
    app()
