print("Ця програма виконує математичні дії")

try:
    num1 = float(input("Введіть перше число: "))
    operator = input("Введіть дію (+, -, *, /): ")
    num2 = float(input("Введіть друге число: "))

    if operator == '+':
        result = num1 + num2
    if operator == '-':
        result = num1 - num2
    if operator == '*':
        result = num1 * num2
    if operator == '/':
        if num2 == 0:
            print("Помилка: Ділення на нуль неіснує!")
        else:
            result = num1 / num2
    else:
        print("Невірна операція. Використовуйте +, -, * або /.")

    if operator in ('+', '-', '*', '/') and not (operator == '/' and num2 == 0):
        print(f"Результат: {num1} {operator} {num2} = {result}")

except ValueError:
    print("Помилка: Введіть правильні числа!")
