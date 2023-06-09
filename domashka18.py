# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X .
# Если таких значений больше одного, вывести первый найденный.

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

# количество элементов в массиве
n = int(input('Введите количество элементов в массиве: '))
a = list(map(int, input('Введите значения масива через пробел: ').split()))  # сам массив
x = int(input('Искомое число: '))  # искомое число

min_diff = abs(a[0] - x)  # наименьшее расстояние до X
closest = a[0]  # ближайший элемент к X

for i in range(1, n):
    diff = abs(a[i] - x)
    if diff < min_diff:
        min_diff = diff
        closest = a[i]

print(closest)
