import tkinter as tk
from tkinter import messagebox
from classes import Task, TaskManager


class TaskManagerApp:
    def __init__(self, root):
        self.manager = TaskManager()
        self.root = root
        self.root.title("Менеджер задач")
        self.root.geometry("500x400")
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Название").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.title_entry = tk.Entry(self.root, width=40)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Описание").grid(row=1, column=0, padx=5, pady=5, sticky="nw")
        self.desc_text = tk.Text(self.root, height=4, width=30)
        self.desc_text.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Срок (ГГГГ-ММ-ДД)").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.date_entry = tk.Entry(self.root, width=40)
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        btn_frame = tk.Frame(self.root)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=10)

        tk.Button(btn_frame, text="Добавить задачу", command=self.add_task, width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Удалить задачу", command=self.delete_task, width=15).pack(side=tk.LEFT, padx=5)

        tk.Label(self.root, text="Список задач:").grid(row=4, column=0, columnspan=2, sticky="w", padx=5)

        self.tasks_listbox = tk.Listbox(self.root, width=60, height=12)
        self.tasks_listbox.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.update_listbox()

    def add_task(self):
        title = self.title_entry.get().strip()
        description = self.desc_text.get("1.0", tk.END).strip()
        due_date = self.date_entry.get().strip()

        if title and description and due_date:
            task = Task(title, description, due_date)
            self.manager.add_task(task)
            self.update_listbox()
            self.clear_inputs()
        else:
            messagebox.showwarning("Ошибка", "Заполните все поля!")

    def delete_task(self):
        selected = self.tasks_listbox.curselection()
        if selected:
            self.manager.delete_task(selected[0])
            self.update_listbox()
        else:
            messagebox.showwarning("Ошибка", "Выберите задачу для удаления!")

    def update_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.manager.tasks:
            self.tasks_listbox.insert(tk.END, f"{task.title} (до {task.due_date})")

    def clear_inputs(self):
        self.title_entry.delete(0, tk.END)
        self.desc_text.delete("1.0", tk.END)
        self.date_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
