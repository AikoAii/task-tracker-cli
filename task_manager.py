from datetime import datetime
from storage import load_tasks, save_tasks

def _timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def _next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def add_task(description):
    tasks = load_tasks()
    task = {
        "id": _next_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": _timestamp(),
        "updatedAt": _timestamp()
    }
    tasks.append(task)
    save_tasks(tasks)
    return task["id"]

def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = _timestamp()
            save_tasks(tasks)
            return True
    return False

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        return False
    save_tasks(new_tasks)
    return True

def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = _timestamp()
            save_tasks(tasks)
            return True
    return False

def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        return [t for t in tasks if t["status"] == status]
    return tasks
