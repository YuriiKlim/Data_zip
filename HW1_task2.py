# Завдання 2
# Маємо певний словник з назвами музичних груп (виконавців) та альбомів. Назва групи використовується як ключ,
# назва альбомів — як значення. Реалізуйте: додавання, видалення, пошук, редагування, збереження та завантаження
# даних (використовуючи стиснення та розпакування).
import pickle
import gzip


class MusicCatalog:
    def __init__(self):
        self.catalog = {}

    def add_artist(self, artist):
        if artist not in self.catalog:
            self.catalog[artist] = set()
            print(f"Додано нового артиста {artist}.")
        else:
            print("Цей артист уже існує.")

    def delete_artist(self, artist):
        if artist in self.catalog:
            del self.catalog[artist]
            print(f"Артист {artist} видалений.")
        else:
            print("Артиста не знайдено.")

    def find_album(self, album_name):
        found = False
        for artist, albums in self.catalog.items():
            if album_name in albums:
                print(f"Альбом '{album_name}' належить артисту {artist}.")
                found = True
        if not found:
            print("Альбом не знайдено.")

    def add_album(self, artist, album):
        if artist in self.catalog:
            if album in self.catalog[artist]:
                print("Цей альбом вже існує.")
            else:
                self.catalog[artist].add(album)
                print(f"Альбом '{album}' додано до артиста {artist}.")
        else:
            print("Артиста не знайдено, спочатку додайте артиста.")

    def delete_album(self, artist, album):
        if artist in self.catalog:
            if album in self.catalog[artist]:
                self.catalog[artist].remove(album)
                print(f"Альбом '{album}' видалено.")
            else:
                print("Такого альбому не знайдено.")
        else:
            print("Артиста не знайдено.")

    def save_catalog(self, filename):
        with gzip.open(filename, 'wb') as file:
            pickle.dump(self.catalog, file)
        print("Каталог збережено.")

    def load_catalog(self, filename):
        try:
            with gzip.open(filename, 'rb') as file:
                self.catalog = pickle.load(file)
            print("Каталог завантажено.")
        except Exception as e:
            print("Помилка при завантаженні каталогу:", e)

    def display_all(self):
        if not self.catalog:
            print("Список користувачів порожній.")
        else:
            for artist, albums in self.catalog.items():
                print(f"Виконавець: {artist}, Альбом: {albums}")



def main_menu():
    catalog = MusicCatalog()

    while True:
        print("\n1. Додати виконавця")
        print("2. Видалити виконавця")
        print("3. Додати альбом")
        print("4. Знайти альбом")
        print("5. Видалити альбом")
        print("6. Зберегти дані")
        print("7. Завантажити дані")
        print("8. Відобразити дані")
        print("9. Вихід")

        choice = input("Оберіть опцію: ")

        if choice == "1":
            catalog.add_artist(input("Введіть виконавця: "))
        elif choice == "2":
            catalog.delete_artist(input("Введіть виконавця: "))
        elif choice == "3":
            catalog.add_album(input("Введіть виконавця: "), input("Введіть назву альбому: "))
        elif choice == "4":
            catalog.find_album(input("Введіть назву альбому: "))
        elif choice == "5":
            catalog.delete_album(input("Введіть виконавця: "), input("Введіть назву альбому: "))
        elif choice == "6":
            catalog.save_catalog("music_catalog.gz")
        elif choice == "7":
            catalog.load_catalog("music_catalog.gz")
        elif choice == "8":
            catalog.display_all()
        elif choice == "9":
            break
        else:
            print("Невірний вибір")


main_menu()
