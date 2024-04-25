# Завдання 2
# Реалізація програми для додавання, видалення та
# відстеження завдань/заміток. Зберігати ці завдання у
# форматі JSON у файлі. Можливість завантаження
# раніше збережених завдань для подальшої роботи з
# ними.
import json


class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task_name, task_details):
        self.tasks[task_name] = task_details
        self.save_tasks()
        print(f"Завдання '{task_name}' додано.")

    def delete_task(self, task_name):
        if task_name in self.tasks:
            del self.tasks[task_name]
            self.save_tasks()
            print(f"Завдання '{task_name}' видалено.")
        else:
            print(f"Завдання '{task_name}' незнайдено.")

    def show_tasks(self):
        if self.tasks:
            for task_name, details in self.tasks.items():
                print(f"{task_name}: {details}")
        else:
            print("Немає завдань.")


def main_menu():
    manager = TaskManager()
    while True:
        print("\n1. Показати завдання")
        print("2. Додати завдання")
        print("3. Видалити завдання")
        print("4. Вийти")
        choice = input("Виберіть опцію: ")

        if choice == '1':
            manager.show_tasks()
        elif choice == '2':
            task_name = input("Введіть назву завдання: ")
            task_details = input("Введіть деталі завдання: ")
            manager.add_task(task_name, task_details)
        elif choice == '3':
            task_name = input("Введіть назву завдання для видалення: ")
            manager.delete_task(task_name)
        elif choice == '4':
            break
        else:
            print("Невірний вибір .")


if __name__ == '__main__':
    main_menu()
