# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

import random

print("Введите количество элементов массива: ", end =" ")
N = int(input())
my_list =[]
for i in range(N):
    x1 = random.randint(0, 10)
    my_list. append(x1)
print(*my_list)
