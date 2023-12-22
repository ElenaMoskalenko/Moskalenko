# Дан список размера N и целые числа K и L (1 < K < L < N ). Найти среднее
# арифметическое элементов списка с номерами от K до L включительно.

def find_average(lst, k, l):
    sublist = lst[k-1:l]
    average = sum(sublist) / len(sublist)
    return average
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 2
l = 5
result = find_average(lst, k, l)
print("Среднее арифметическое элементов списка с номерами от", k, "до", l, "включительно: ", result)
