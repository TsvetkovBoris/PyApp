# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
import random

print("Введите количество монеток:", end=" ")
n = int(input())
count1 = 0
count2 = 0
print("Введите 0 или 1")
for i in range (n):
    temp = int(input())
    if temp == 0:
        count1 += 1
    else:
        count2 += 1
if count1 >= count2:
    print("\nМонеток нужно перевернуть -", count2)
else:
    print("\nМонеток нужно перевернуть -", count1)

""" myArray = [0] * n
for i in range(len(myArray)):
    myArray[i] = random.randint(0, 1)
    print(myArray[i], end=" ")
    if myArray[i] == 0:
        count1 += 1
    else:
        count2 += 1
if count1 >= count2:
    print("\nМонеток нужно перевернуть -", count2)
else:
    print("\nМонеток нужно перевернуть -", count1)
    """

