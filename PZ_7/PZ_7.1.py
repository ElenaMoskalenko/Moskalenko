# Дано целое положительное число. Вывести символы, изображающие цифры этого
# числа (в порядке слева направо).
def print_digits(num):
    digits = str(num)
    for digit in digits:
        print(digit)
num = int(input("Введите целое положительное число: "))
print_digits(num)
