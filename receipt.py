def calculate_total(items, discount=0, tax=0):
    if not items:
        raise ValueError("Пустая корзина")

    if discount > 50:
        raise ValueError("Слишком большая скидка")

    total = 0
    for name, price in items:
        if price < 0:
            raise ValueError("Отрицательная цена")
        total += price

    total *= (1 - discount / 100)
    total *= (1 + tax / 100)

    return round(total, 2)


def generate_receipt(items, payment_method):
    total = calculate_total(items)

    receipt = "ЧЕК\n"
    for name, price in items:
        receipt += f"{name}: {price}\n"

    receipt += f"Итого: {total}\n"
    receipt += f"Оплата: {payment_method}"

    return receipt