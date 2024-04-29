# Завдання 3
# До вже реалізованого класу «Стадіон» додайте можливість
# стиснення та розпакування даних з використанням json та
# pickle.
import datetime
import re
import json
import pickle


class Person:
    object_count = 0
    def __init__(self, full_name="", date_of_birth="", phone="", city="", country="", address=""):
        self.full_name = full_name
        self.date_of_birth = datetime.datetime.strptime(date_of_birth, "%d.%m.%Y").date() if date_of_birth else None
        self.phone = phone
        self.city = city
        self.country = country
        self.address = address
        Person.object_count += 1

    @staticmethod
    def input_alpha_data(prompt):
        while True:
            value = input(prompt)
            if value.replace(' ','').isalpha():
                return value
            else:
                print("Неправильне значення. Будь ласка, введіть лише букви.")

    @staticmethod
    def input_date_of_birth(prompt="Введіть дату народження (дд.мм.рррр): "):
        while True:
            date_input = input(prompt)
            try:
                return datetime.datetime.strptime(date_input, "%d.%m.%Y").date()
            except ValueError:
                print("Невірний формат дати. Спробуйте ще раз.")

    @staticmethod
    def input_phone(prompt="Введіть контактний телефон у форматі '+12345678': "):
        phone_pattern = r"^\+\d+$"
        while True:
            phone_input = input(prompt)
            if re.match(phone_pattern, phone_input):
                return phone_input
            else:
                print("Невірний формат телефонного номера. Спробуйте ще раз.")

    def input_data(self):
        self.full_name = Person.input_alpha_data("\nВведіть ПІБ: ")
        self.date_of_birth = Person.input_date_of_birth()
        self.phone = Person.input_phone()
        self.city = Person.input_alpha_data("Введіть місто: ")
        self.country = Person.input_alpha_data("Введіть країну: ")
        self.address = input("Введіть домашню адресу: ")

    def display_data(self):
        print("\nДані про людину:")
        print(f"ПІБ: {self.full_name}")
        dob = self.date_of_birth.strftime('%d.%m.%Y') if self.date_of_birth else "Не вказано"
        print(f"Дата народження: {dob}")
        print(f"Контактний телефон: {self.phone}")
        print(f"Місто: {self.city}")
        print(f"Країна: {self.country}")
        print(f"Домашня адреса: {self.address}")

    def __lt__(self, other):
        if self.date_of_birth and other.date_of_birth:
            return self.date_of_birth > other.date_of_birth
        return False

    def __eq__(self, other):
        return len(self.full_name) == len(other.full_name)

    def compare_names(self, other):
        return len(self.full_name) > len(other.full_name)

    def city_first_alphabetically(self, other):
        return self.city < other.city

    def country_first_alphabetically(self, other):
        return self.country < other.country

    @staticmethod
    def get_object_count():
        return Person.object_count

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump({
                'full_name': self.full_name,
                'date_of_birth': self.date_of_birth.strftime('%d.%m.%Y') if self.date_of_birth else None,
                'phone': self.phone,
                'city': self.city,
                'country': self.country,
                'address': self.address
            }, file)

    @classmethod
    def load_from_json(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            obj = cls()
            obj.full_name = data['full_name']
            obj.date_of_birth = datetime.datetime.strptime(data['date_of_birth'], "%d.%m.%Y").date() if data[
                'date_of_birth'] else None
            obj.phone = data['phone']
            obj.city = data['city']
            obj.country = data['country']
            obj.address = data['address']
            return obj

    def save_to_pickle(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_from_pickle(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)


person1 = Person()
person2 = Person()
person1.input_data()
person2.input_data()
person1.display_data()
person2.display_data()
person1.save_to_json("person1.json")
person2.save_to_json("person2.json")
person1.save_to_pickle("person1.pickle")
person2.save_to_pickle("person2.pickle")
person1.load_from_pickle("person1.pickle")
person2.load_from_pickle("person2.pickle")
person1.load_from_json("person1.json")
person2.load_from_json("person2.json")
print(f"\nКількість створених об'єктів 'Людина':{Person.get_object_count()}")

print("Хто старший:", f"{person1.full_name}" if person2 < person1 else f"{person2.full_name}")
print("У кого довший ПІБ:", f"{person1.full_name}" if person1.compare_names(person2) else f"{person2.full_name}")
print("Чиє місто йде першим у алфавітному порядку:", f"{person1.full_name}" if person1.city_first_alphabetically(person2) else f"{person2.full_name}")
print("Чия країна йде перша у алфавітному порядку:", f"{person1.full_name}" if person1.country_first_alphabetically(person2) else f"{person2.full_name}")