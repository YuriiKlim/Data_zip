# Завдання 1
# Створіть два окремих "мікросервіси" (дві окремі
# програми). Одна програма створює та експортує дані у
# форматі JSON, а інша програма завантажує та обробляє ці
# дані. Це може бути, наприклад, система, яка створює та
# обробляє замовлення.
import json

#Створення даних
def create_order():
    while True:
        try:
            name = input("Введіть назву товару: ")
            quantity = int(input("Введіть кількість товару: "))
            price = float(input("Введіть ціну за одиницю: "))
            break
        except ValueError:
            print("Неправильне значення")
    return {
        'name': name,
        'quantity': quantity,
        'price': price
    }


def save_orders(orders, filename='orders.json'):
    with open(filename, 'w') as file:
        json.dump(orders, file)


def main_export():
    orders = []
    while True:
        print("\n1. Додати замовлення")
        print("2. Експортувати замовлення та вийти")
        choice = input("Оберіть опцію: ")
        if choice == '1':
            order = create_order()
            orders.append(order)
        elif choice == '2':
            save_orders(orders)
            print("Замовлення експортовано.")
            break
        else:
            print("Невідома опція. Спробуйте знову.")


if __name__ == '__main__':
    main_export()

#Завантаження даних
def load_orders(filename='orders.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Файл не знайдено.")
        return []


def process_orders(orders):
    total_cost = sum(order['quantity'] * order['price'] for order in orders)
    print(f"Загальна вартість усіх замовлень: {total_cost:.2f}")


def main_import():
    orders = load_orders()
    if orders:
        process_orders(orders)
    else:
        print("Немає замовлень для обробки.")


if __name__ == '__main__':
    main_import()

