# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

print("Введите количество всех журавликов")
S = int(input())
K = S // 3 * 2
P = S // 3 // 2
print(f"Петя и Сережа сделали {P} журавликов")
print(f"Катя сделала {K} журавликов")