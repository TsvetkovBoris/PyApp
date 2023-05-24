# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import math

print("Введите любое число: ", end=" ")
N = int(input())
for i in range (0, N):
    numPow = math.pow(2, i)
    if numPow < N:
        print(math.trunc(numPow), end=" ")
