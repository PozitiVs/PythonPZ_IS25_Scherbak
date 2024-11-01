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
