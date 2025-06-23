try:
    number_str = input("Введіть чотиризначне число: ")
    number = int(number_str)

    if 1000 <= number <= 9999:
        digit1 = number // 1000
        digit2 = (number % 1000) // 100
        digit3 = (number % 100) // 10
        digit4 = number % 10

        print(digit1)
        print(digit2)
        print(digit3)
        print(digit4)
    else:
        print("Ви ввели не чотиризначне число.")

except ValueError:
    print("Ви ввели не ціле число.")

