# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

import random

N = int(input("Введите количество элементов массива: "))
my_list = []
number = 0
for i in range(N):
    x1 = random.randint(0, 100)
    my_list. append(x1)
print(*my_list)
X = int(input("Введите число Х: "))
min_raz = abs(my_list[0] - X)
for i in range(N):
    count = abs(my_list[i] - X)
    if min_raz > count:
        min_raz = count
        number = i
print(f'Самый близкий по величине элемент = {my_list[number]}')