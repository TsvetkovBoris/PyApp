# Задача 2: Найдите сумму цифр трехзначного числа.
print("Введите трехзначное число: ")
number = int(input())
first = number // 100
second = number // 10 % 10
third = number % 10
summ = first + second + third
print(f"Сумма цифр трехзначного числа {number} = ", summ)
