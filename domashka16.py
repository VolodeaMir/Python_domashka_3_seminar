# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

n = int(input('Введите количество элементов в массиве: '))
a = list(map(int, input('Введите значения масива через пробел: ').split()))
x = int(input('Искомое число: '))

count = 0  # счетчик количества вхождений числа X в массив A

for i in range(n):
    if a[i] == x:
        count += 1

print(count)
