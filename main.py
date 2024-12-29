def calculator():
    print("Найпростіший калькулятор")

    while True:
        try:

            num1 = float(input("Введіть перше число: "))
            operation = input("Введіть дію (+, -, *, /): ").strip()
            if operation not in ['+', '-', '*', '/']:
                print("Невідома дія! Спробуйте ще раз.")
                continue
            num2 = float(input("Введіть друге число: "))
            if operation == '/' and num2 == 0:
                print("Помилка: ділити на нуль неможна!")
                continue
            if operation == '+':
                print (f"Результат: {num1 + num2}")
            elif operation == '-':
                print (f"Результат: {num1 - num2}")
            elif operation == '*':
                print (f"Результат: {num1 * num2}")
            elif operation == '/':
                print (f"Результат: {num1 / num2}")
        except ValueError:
            print("Помилка!!!")


if __name__ == "__main__":
    calculator()
