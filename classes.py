import json


class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_from_file()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_to_file()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_to_file()

    def save_to_file(self):
        data = []
        for task in self.tasks:
            data.append({
                "title": task.title,
                "description": task.description,
                "due_date": task.due_date
            })
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_from_file(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.tasks = []
                for item in data:
                    task = Task(
                        item["title"],
                        item["description"],
                        item["due_date"]
                    )
                    self.tasks.append(task)
        except FileNotFoundError:
            self.tasks = []
        except Exception:
            self.tasks = []
