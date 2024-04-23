# Завдання 3
# Маємо певний словник з логінами і паролями користувачів. Логін використовується як ключ, пароль —
# як значення. Реалізуйте: додавання, видалення, пошук,
# редагування, збереження та завантаження даних (використовуючи стиснення та розпакування).
import gzip
import pickle


class UserCredentials:
    def __init__(self):
        self.credentials = {}

    def add_user(self, username, password):
        if username in self.credentials:
            print("Користувач з таким логіном вже існує.")
        else:
            self.credentials[username] = password
            print("Новий користувач доданий.")

    def delete_user(self, username):
        if username in self.credentials:
            del self.credentials[username]
            print("Користувач видалений.")
        else:
            print("Користувач не знайдений.")

    def find_user(self, username):
        if username in self.credentials:
            print(f"Користувач {username} існує.")
        else:
            print("Користувач не знайдений.")

    def update_password(self, username, new_password):
        if username in self.credentials:
            self.credentials[username] = new_password
            print("Пароль оновлено.")
        else:
            print("Користувач не знайдений.")

    def save_data(self, file_path):
        with gzip.open(file_path, 'wb') as file:
            pickle.dump(self.credentials, file)
        print("Дані збережено.")

    def load_data(self, file_path):
        try:
            with gzip.open(file_path, 'rb') as file:
                self.credentials = pickle.load(file)
            print("Дані завантажено.")
        except FileNotFoundError:
            print("Файл не знайдено.")
        except EOFError:
            print("Файл порожній.")

    def display_all_users(self):
        if not self.credentials:
            print("Список користувачів порожній.")
        else:
            for username, password in self.credentials.items():
                print(f"Користувач: {username}, Пароль: {password}")


def main_menu():
    user_data = UserCredentials()

    while True:
        print("\n1. Додати користувача")
        print("2. Видалити користувача")
        print("3. Знайти користувара")
        print("4. Оновити пароль")
        print("5. Зберегти данні")
        print("6. Завантажити данні")
        print("7. Відобразити усіх користувачів")
        print("8. Вихід")

        choice = input("Оберіть опцію: ")

        if choice == "1":
            user_data.add_user(input("Введіть логін: "), input("Введіть пароль: "))
        elif choice == "2":
            user_data.delete_user(input("Введіть логін: "))
        elif choice == "3":
            user_data.find_user(input("Введіть логін: "))
        elif choice == "4":
            user_data.update_password(input("Введіть логін: "), input("Введіть пароль: "))
        elif choice == "5":
            user_data.save_data("credentials.gz")
        elif choice == "6":
            user_data.load_data("credentials.gz")
        elif choice == "7":
            user_data.display_all_users()
        elif choice == "8":
            break
        else:
            print("Невірний вибір")


main_menu()

