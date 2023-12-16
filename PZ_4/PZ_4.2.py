# Дано целое число N (> 0). Найти сумму 1^1 2^2 + … + N^N

try:
    def calculate_sum_of_powers(N):
        sum_of_powers = 0
        for i in range(1, N+1):
            sum_of_powers += i**i
        return sum_of_powers

    N = int(input("Введите целое число N: "))
    result = calculate_sum_of_powers(N)
    print(f"Сумма степеней равна: {result}")
except ValueError:
    print("Проверьте правильность введенных данных")