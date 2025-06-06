#Сгенерировать двумерный список в котором элементы >= 10 заменяются на 0
import random

matrix = [[random.randint(1, 15) for _ in range(5)] for _ in range(4)]
processed = list(map(lambda row: list(map(lambda x: 0 if x >= 10 else x, row)), matrix))

print("Исходная матрица:")
for row in matrix:
    # Форматируем вывод, чтобы числа выравнивались по правому краю
    print(" ".join(f"{num}" for num in row))

print("\nОбработанная матрица (числа >= 10 заменены на 0):")
for row in processed:
    print(" ".join(f"{num}" for num in row))