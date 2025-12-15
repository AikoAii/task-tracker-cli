#!/usr/bin/env python3

import sys
from task_manager import (
    add_task,
    update_task,
    delete_task,
    mark_task,
    list_tasks
)

def main():
    if len(sys.argv) < 2:
        print("No command provided")
        return

    command = sys.argv[1]

    try:
        if command == "add":
            task_id = add_task(sys.argv[2])
            print(f"Task added (ID: {task_id})")

        elif command == "update":
            ok = update_task(int(sys.argv[2]), sys.argv[3])
            print("Task updated" if ok else "Task not found")

        elif command == "delete":
            ok = delete_task(int(sys.argv[2]))
            print("Task deleted" if ok else "Task not found")

        elif command == "mark-in-progress":
            ok = mark_task(int(sys.argv[2]), "in-progress")
            print("Updated" if ok else "Task not found")

        elif command == "mark-done":
            ok = mark_task(int(sys.argv[2]), "done")
            print("Updated" if ok else "Task not found")

        elif command == "list":
            status = sys.argv[2] if len(sys.argv) > 2 else None
            tasks = list_tasks(status)
            if not tasks:
                print("No tasks found")
                return
            for t in tasks:
                print(f"[{t['id']}] {t['description']} | {t['status']}")

        else:
            print("Unknown command")

    except (IndexError, ValueError):
        print("Invalid arguments")

if __name__ == "__main__":
    main()
