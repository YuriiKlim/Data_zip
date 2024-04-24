# Завдання 1
# Маємо певний словник з назвами країн і столиць. Назва
# країни використовується як ключ, назва столиці — як значення. Реалізуйте: додавання, видалення, пошук, редагування,
# збереження та завантаження даних (використовуючи стиснення та розпакування).
import pickle
import gzip


class CountryCapital:
    def __init__(self):
        self.data = {}

    def add_country(self, country, capital):
        if country in self.data:
            print("Країна вже існує в базі даних.")
        else:
            self.data[country] = capital
            print(f"Додано {country} зі столицею {capital}.")

    def delete_country(self, country):
        if country in self.data:
            del self.data[country]
            print(f"Країна {country} видалена.")
        else:
            print("Країна не знайдена.")

    def find_capital(self, country):
        capital = self.data.get(country)
        if capital:
            print(f"Столиця країни {country} — {capital}.")
        else:
            print("Країна не знайдена.")

    def update_capital(self, country, new_capital):
        if country in self.data:
            self.data[country] = new_capital
            print(f"Столицю країни {country} оновлено на {new_capital}.")
        else:
            print("Країна не знайдена.")

    def save_data(self, file_path):
        with gzip.open(file_path, 'wb') as file:
            pickle.dump(self.data, file)
        print("Дані збережено успішно.")

    def load_data(self, file_path):
        try:
            with gzip.open(file_path, 'rb') as file:
                self.data = pickle.load(file)
            print("Дані завантажено успішно.")
        except FileNotFoundError:
            print("Файл не знайдено.")
        except EOFError:
            print("Файл порожній або пошкоджений.")

    def display_all(self):
        if not self.data:
            print("Список користувачів порожній.")
        else:
            for country, capital in self.data.items():
                print(f"Користувач: {country}, Пароль: {capital}")


def main_menu():
    db = CountryCapital()

    while True:
        print("\n1. Додати країну")
        print("2. Видалити країну")
        print("3. Знайти столицю")
        print("4. Оновити столицю")
        print("5. Зберегти дані")
        print("6. Завантажити дані")
        print("7. Відобразити дані")
        print("8. Вихід")

        choice = input("Оберіть опцію: ")

        if choice == "1":
            db.add_country(input("Введіть назву країни: "), input("Введіть столицю країни: "))
        elif choice == "2":
            db.delete_country(input("Введіть назву країни: "))
        elif choice == "3":
            db.find_capital(input("Введіть країну: "))
        elif choice == "4":
            db.update_capital(input("Введіть стару столицю: "), input("Введіть нову столицю: "))
        elif choice == "5":
            db.save_data("countrys.gz")
        elif choice == "6":
            db.load_data("countrys.gz")
        elif choice == "7":
            db.display_all()
        elif choice == "8":
            break
        else:
            print("Невірний вибір")


main_menu()

