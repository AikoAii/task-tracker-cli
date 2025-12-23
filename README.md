# Task Tracker CLI

```txt
simple CLI | python | json | terminal  ( •̀ ω •́ )✧
```

A small, fun, and slightly *fun-coded* **command-line task tracker** built with Python.
No frameworks, no dependencies — just pure Python, JSON, and terminal vibes.

Light, clean, and made for small experiments in the terminal.

---

## ✨ Features

```txt
[✓] Add tasks
[✓] Update tasks
[✓] Delete tasks
[✓] Mark status: todo / in-progress / done
[✓] List & filter tasks
```

All tasks are stored locally in a simple JSON file.

---

## 📦 Requirements

```bash
python >= 3.x
terminal (any OS)
```

No external libraries. No setup drama.

---

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/AikoAii/task-tracker-cli.git
cd task-tracker-cli
```

(Optional, but nice):

```bash
chmod +x task_cli.py
```

---

## 🧪 Usage

### ➕ Add a task

```bash
python task_cli.py add "Buy groceries"
```

### ✏️ Update a task

```bash
python task_cli.py update 1 "Buy groceries and cook dinner"
```

### 🗑 Delete a task

```bash
python task_cli.py delete 1
```

### 🔄 Change task status

```bash
python task_cli.py mark-in-progress 1
python task_cli.py mark-done 1
```

### 📋 List all tasks

```bash
python task_cli.py list
```

### 🎯 Filter by status

```bash
python task_cli.py list todo
python task_cli.py list in-progress
python task_cli.py list done
```

---

## 🗂 Task Data Structure

```json
{
  "id": 1,
  "description": "Buy groceries",
  "status": "todo",
  "createdAt": "2025-12-15 09:00:00",
  "updatedAt": "2025-12-15 09:00:00"
}
```

`tasks.json` will be created automatically after adding your first task.

---

## 🧼 Notes

```txt
- no external dependencies
- Python standard library only
- simple error handling
- readable and easy to hack
```

---

## 📄 License

MIT License — free to use, modify, remix, and experiment.

---

## 🎯 Why this project?

```txt
- practice building CLI tools
- learn file & JSON handling
- keep things small and clean
- build something actually usable
```

Small project, real practice.

---

```txt
have fun:3
```
