# Завдання 1
# Користувач заповнює з клавіатури список цілих.
# Стисніть отримані дані та збережіть їх у файл. Після цього
# завантажте дані з файлу в новий список.
import pickle


def get_user_input():
    numbers = []
    while True:
        try:
            num = input("Введіть число (або натисніть Enter для завершення): ")
            if num == "":
                break
            numbers.append(int(num))
        except ValueError:
            print("Будь ласка, введіть коректне ціле число.")
    return numbers


def save_data_to_file(data, filename="data.pickle"):
    with open(filename, "wb") as file:
        pickle.dump(data, file)


def load_data_from_file(filename="data.pickle"):
    with open(filename, "rb") as file:
        return pickle.load(file)


def main():
    user_data = get_user_input()
    save_data_to_file(user_data)
    loaded_data = load_data_from_file()
    print("Завантажені дані з файлу:", *loaded_data)


if __name__ == "__main__":
    main()
