#Дан список A размера N. Сформировать новый список B того же размера по следующему правилу:
#элемент BK равен среднему арифметическому элементов списка A с номерами от 1 до K.
def calculate(A):
    a_sum = 0
    B = []
    count = 0

    for element in A:
        try:
            count += 1
            a_sum += element
            ge = a_sum / count
            B.append(ge)
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль.")
            B.append(0)  # Или другое значение по вашему выбору
    return B

A = [2, 4, 6, 8] 
B = calculate(A)
print(B)  