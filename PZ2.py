<<<<<<< HEAD:PZ2.py
#Надо найти число полных отрезков на прямой А
#Для этого надо использовать деление нацело
print("Введите 2 числа (A>B)")
A = int(input())
B = int(input())
try:
    if A<=0 or B<=0:
        print("A и B должны быть положительными")
    elif A<B:
        print("A < B -> число отрезков = 0")
    else:
        print("Число отрезков:", A//B)
except:
    print("Произошла ошибка")
=======
print("Введите 2 числа (A>B)")
A = int(input())
B = int(input())
try:
    if A<=0 or B<=0:
        print("A и B должны быть положительными")
    elif A<B:
        print("A < B -> число отрезков = 0")
    else:
        print("Число отрезков:", A//B)
except:
    print("Произошла ошибка")
>>>>>>> e2d4503b22b8373eec460f19d65fb83cf9488457:PZ/PZ2.py
