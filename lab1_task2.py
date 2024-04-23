# Завдання 2
# При старті програми з’являється меню з наступними
# пунктами:
# 1. Завантаження даних;
# 2. Збереження даних;
# 3. Додавання даних;
# 4. Видалення даних.
# Використайте список цілих як сховища даних. Також
# застосуйте стиснення/розпакування даних.
import gzip
import pickle

data = []

def load_data():
    try:
        with gzip.open('data.gz', 'rb') as f:
            global data
            data = pickle.load(f)
        print("Дані завантажено успішно.")
    except FileNotFoundError:
        print("Файл не знайдено.")

def save_data():
    with gzip.open('data.gz', 'wb') as f:
        pickle.dump(data, f)
    print("Дані збережено успішно.")

def add_data():
    while True:
        try:
            number = int(input("Введіть число для додавання: "))
            data.append(number)
            break
        except ValueError:
            print("Будь ласка, введіть коректне число.")

def delete_data():
    while True:
        try:
            number = int(input("Введіть число для видалення: "))
            data.remove(number)
            print(f"Число {number} видалено.")
            break
        except ValueError:
            print("Будь ласка, введіть коректне число.")
        except Exception as e:
            print(str(e))

def display_data():
    if data:
        print("Поточні дані у файлі:")
        for num in data:
            print(num)
    else:
        print("Список порожній.")

def main_menu():
    while True:
        print("\n1. Завантаження даних")
        print("2. Збереження даних")
        print("3. Додавання даних")
        print("4. Видалення даних")
        print("5. Показати дані")
        print("6. Вийти з програми")
        choice = input("Оберіть опцію: ")

        if choice == '1':
            load_data()
        elif choice == '2':
            save_data()
        elif choice == '3':
            add_data()
        elif choice == '4':
            delete_data()
        elif choice == '5':
            display_data()
        elif choice == '6':
            break
        else:
            print("Невірний вибір, спробуйте знову.")


if __name__ == "__main__":
    main_menu()
