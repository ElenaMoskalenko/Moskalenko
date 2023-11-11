# Даны два числа. Вывести вначале большее, а затем меньшее из них
try:
    num1, num2 = float(input('Введите первое число: ')), float(input('Введите второе число: '))
    if num1 > num2:
            print(num1, num2)
    else:
            print(num2, num1)
except ValueError:
    print('Введите верные числа')
