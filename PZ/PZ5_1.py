#Использовать функцию найти сумму ряда от 1 до 60
#Использовать локальные переменные
def sum(n):
    total_sum = 0  
    number = 1  
    while number <= n:
        total_sum += number
        number += 1  
    return total_sum
N = 60 
result = sum(N)
print("Сумма ряда от 1 до 60 равна:", result)
