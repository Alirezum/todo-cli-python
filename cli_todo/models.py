from dataclasses import dataclass
from datetime import datetime


@dataclass()
class Task:
    id: int | None
    title: str
    description: str = ""
    due_date: datetime | None = None
    completed: bool = False

    def __str__(self):
        status = f"Done" if self.completed else "Pending"
        due = self.due_date.isoformat() if self.due_date else "No due"
        return f"{[self.id]} | {self.title} - {status} - ( due : {due})"
