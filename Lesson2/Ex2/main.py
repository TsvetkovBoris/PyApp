# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import math
print("Введите сумму:", end=" ")
S = int(input())
print("Введите произведение:", end=" ")
P = int(input())
D = S * S - 4 * P
X = (-S + math.sqrt(D)) / 2
Y = (-S - math.sqrt(D)) / 2
print("Первое число =", math.fabs(X))
print("Второе число =", math.fabs(Y))