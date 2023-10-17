def check_opposite_numbers(num1, num2, num3):
    if (num1 == -num2) or (num1 == -num3) or (num2 == -num3):
        return True
    else:
        return False

# Пример использования функции
number1 = 5
number2 = -5
number3 = 10

if check_opposite_numbers(number1, number2, number3):
    print("Среди трех данных чисел есть хотя бы одна пара взаимно противоположных.")
else:
    print("Среди трех данных чисел нет пар взаимно противоположных.")