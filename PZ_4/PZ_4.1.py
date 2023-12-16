# Дано вещественное число X и целое число N (> 0).
# Найти значение выражения 1 - X^2/(2!) + X^4/(4!) - ... + (-1)^N-X^2*N/((2-N)!) (N! = 12 ...N).
# Полученное число является приближенным значением функции cos в точке X.

import math
try:
    X = float(input('Введите число X: '))
    N = int(input('Введите число N: '))
    result = 1
    sign = -1
    power = 2
    factorial = 2

    for i in range(1, N + 1):
        result += sign * (X ** power) / math.factorial(factorial)
        sign *= -1
        power += 2
        factorial += 2

    print('Приближенное значение функции cos в точке X = ', result)
except ValueError:
    print("Проверьте правильность введенных данных")