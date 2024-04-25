import json
import pickle


class TaskManager:
    def __init__(self, filename='tasks.json', use_pickle=False):
        self.filename = filename
        self.use_pickle = use_pickle
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'rb' if self.use_pickle else 'r') as file:
                if self.use_pickle:
                    return pickle.load(file)
                else:
                    return json.load(file)
        except FileNotFoundError:
            return {}

    def save_tasks(self):
        with open(self.filename, 'wb' if self.use_pickle else 'w') as file:
            if self.use_pickle:
                pickle.dump(self.tasks, file)
            else:
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
    manager = TaskManager(use_pickle=True)
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
