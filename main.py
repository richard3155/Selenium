def integral():
    try:
        a = float(input("Введите начало интервала: "))
        b = float(input("Введите конец интервала: "))
        n = int(input("Введите количество разбиений: "))

        if n <= 0:
            print("Ошибка: n должно быть > 0")
            return

        h = (b - a) / n
        result = 0

        for i in range(n):
            x = a + i * h
            result += x ** 2

        result *= h
        print(f"Результат интеграла: {result}")

    except ValueError:
        print("Ошибка ввода")


def probability():
    try:
        m = float(input("Введите m: "))
        n = float(input("Введите n: "))

        if n == 0:
            print("Ошибка: n не может быть 0")
            return

        print(f"P = {m / n}")

    except ValueError:
        print("Ошибка ввода")


def gcd():
    try:
        a = int(input("Введите a: "))
        b = int(input("Введите b: "))

        while b != 0:
            a, b = b, a % b

        print(f"НОД: {abs(a)}")

    except ValueError:
        print("Ошибка ввода")


def main():
    while True:
        print("\n1 - Интеграл")
        print("2 - Вероятность")
        print("3 - НОД")
        print("0 - Выход")

        choice = input("Выберите: ")

        if choice == "1":
            integral()
        elif choice == "2":
            probability()
        elif choice == "3":
            gcd()
        elif choice == "0":
            break
        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()