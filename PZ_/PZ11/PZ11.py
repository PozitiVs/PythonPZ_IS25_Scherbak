#средствами языка Python сфрмировать два текстовых файла содержащих по одной последовательности
#из целых положительных или отрицательных чисел. Сформировать новый текстовый файл, предварительно
#сделав требуемую обработку элементов:
#Элементы первого и второго файлов. Кол-во элементов первого и второго файлов.
#Элементы первой трети. Минимальный элемент первой трети.

import random

posit_numbers = []
for i in range(10):
    posit_numbers.append(random.randint(1, 50))
with open('positive.txt', 'w') as file:
    file.write(' '.join(str(num) for num in posit_numbers))

negat_numbers = []
for i in range(10):
    negat_numbers.append(random.randint(-50, -1))
with open('negative.txt', 'w') as file:
    file.write(' '.join(str(num) for num in negat_numbers))

with open('positive.txt', 'r') as file:
    posit_numbers = list(map(int, file.read().split()))
with open('negative.txt', 'r') as file:
    negat_numbers = list(map(int, file.read().split()))

posit_third = posit_numbers[:len(posit_numbers)//3]
negat_third = negat_numbers[:len(negat_numbers)//3]

if posit_third:
    min_positive = min(posit_third)
else:
    min_positive = None
    
if negat_third:
    min_negative = min(negat_third)
else:
    min_negative = None

with open('result.txt', 'w') as file:
    file.write('Положительные числа: ' + str(posit_numbers) + '\n')
    file.write('Количество положительных чисел: ' + str(len(posit_numbers)) + '\n')
    file.write('Первая треть положительных: ' + str(posit_third) + '\n')
    file.write('Минимальное число из первой трети положительных: ' + str(min_positive) + '\n\n')
    
    file.write('Отрицательные числа: ' + str(negat_numbers) + '\n')
    file.write('Количество отрицательных чисел: ' + str(len(negat_numbers)) + '\n')
    file.write('Первая треть отрицательных: ' + str(negat_third) + '\n')
    file.write('Минимальное число из первой трети отрицательных: ' + str(min_negative))
        