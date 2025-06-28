try:
    number1 = float(input("Введіть перше число: "))
    operation = input("Введіть операцію (+, -, *, /): ")
    number2 = float(input("Введіть друге число: "))

    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    elif operation == '/':
        if number2 == 0:
            print("Помилка: Ділення на нуль!")
        else:
            result = number1 / number2
    else:
        print("Помилка: Невірна операція!")
        result = None  # Щоб уникнути невизначеного стану result

    if result is not None:
        print("Результат: ", result)

except ValueError:
    print("Помилка: Некоректний ввід числа!")
except Exception as e:
    print(f"Виникла помилка: {e}")
