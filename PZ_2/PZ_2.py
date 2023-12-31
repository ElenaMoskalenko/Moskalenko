#Скорость первого автомобиля Vi км/ч, второго - V2 км/ч, расстояние между ними S км.
# Определить расстояние между ними через Т часов, если автомобили удаляются друг от друга.
# Данное расстояние равно сумме начального расстояния и общего пути, проделанного автомобилями;
# общий путь = время • суммарная скорость
try:
    V1 = int(input("Введите скорость первого автомобиля (км/ч): "))
    V2 = int(input("Введите скорость второго автомобиля (км/ч): "))
    S = int(input("Введите начальное расстояние между автомобилями (км): "))
    T = int(input("Введите время (ч): "))
    # Вычисляем общую скорость движения автомобилей
    V_total = V1 + V2

    # Вычисляем общий пройденный путь
    distance_total = T * V_total

    # Вычисляем расстояние между автомобилями через T часов
    distance = S + distance_total

    print("Расстояние между автомобилями через", T, "часов:", distance, "км")
except ValueError:
 print("Введите положительные числа")