# Проверить истинность высказывания: «Среди трех данных целых чисел есть хотя бы одна пара взаимно противоположных»
try:
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    num3 = int(input('Введите третье число: '))
    n = False
    if (num1 == -num2) or (num1 == -num3) or (num2 == -num3):
        n = True
    if n:
        print('Среди данных чисел есть пара взаимнопротивоположных')
    else:
        print('Среди данных чисел нет взаимнопротивоположных')
except ValueError:
    print('Введите верные числа')