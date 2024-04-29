# Завдання 2
# Створіть програму для проведення опитування або
# анкетування. Зберігайте відповіді користувачів у форматі
# JSON файлу. Кожне опитування може бути окремим
# об'єктом у файлі JSON, а відповіді кожного користувача -
# списком значень.
import json


class Survey:
    def __init__(self, filename='survey_results.json'):
        self.filename = filename
        self.load_surveys()

    def load_surveys(self):
        try:
            with open(self.filename, 'r', encoding="utf-8") as file:
                self.surveys = json.load(file)
        except FileNotFoundError:
            self.surveys = []

    def save_surveys(self):
        with open(self.filename, 'w', encoding="utf-8") as file:
            json.dump(self.surveys, file, indent=4)

    def conduct_survey(self):
        questions = [
            "Your name",
            "Your age?",
            "Your hobbie?",
            "How are you?"
        ]
        answers = {}
        print("Будь ласка, відповідайте на питання:")
        for question in questions:
            answer = input(question + " ")
            answers[question] = answer

        self.surveys.append(answers)
        self.save_surveys()
        print("Дякуємо за участь у опитуванні!")

    def show_results(self):
        if not self.surveys:
            print("Опитування ще не проводились.")
        for idx, survey in enumerate(self.surveys, 1):
            print(f"\nОпитування №{idx}:")
            for question, answer in survey.items():
                print(f"{question}: {answer}")


def main():
    survey = Survey()
    while True:
        print("\n1. Провести опитування")
        print("2. Показати результати опитувань")
        print("3. Вийти")
        choice = input("Виберіть дію: ")
        if choice == '1':
            survey.conduct_survey()
        elif choice == '2':
            survey.show_results()
        elif choice == '3':
            break
        else:
            print("Невідома опція. Спробуйте знову.")


if __name__ == '__main__':
    main()
