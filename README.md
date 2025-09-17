

# 📝 todo-cli-python

A simple command-line interface (CLI) application for managing your to-do tasks using Python and SQLite.

---

## 📌 Project Description

`todo-cli-python` is a lightweight CLI tool that lets users manage tasks efficiently. Tasks are stored persistently in an SQLite database. You can add, list, and remove tasks directly from the terminal.

---

## 🖼️ Screenshot



---

## ⚡ Features

- Add new tasks with a title and optional description.
    
- List all tasks.
    
- Delete tasks by ID.
    
- Persistent storage using SQLite.
    
- Simple, intuitive command-line interface.
    

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Alirezum/todo-cli-python.git
cd todo-cli-python
```

### 2. Create a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -e .
```

---

## 💻 ## Usage

Below are example usages. Adjust based on the commands in the repository.

|Command|Description|
|---|---|
|`todo add "Buy milk"`|Add a new task with description “Buy milk”|
|`todo list`|Show all pending tasks|
|`todo done <id>`|Mark task with given ID as done|
|`todo remove <id>`|Remove task with given ID|
|`todo list --all`|Show completed + pending tasks|

---

## ✅ Requirements

- Python 3.6+
    
- `tabulate2`
    
- `typer`
    
- `pytest` (for running tests)
    

---

## 🧪 Running Tests

Run tests using `pytest`:

```bash
pytest
```

Make sure `pytest` is installed:

```bash
pip install pytest
```


## License

MIT License — see `LICENSE` file.
