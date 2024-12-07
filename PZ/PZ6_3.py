#Дан список размера N, все элементы которого, кроме последнего, упорядочены по возрастанию.
#Сделать список упорядоченным, переместив последний элемент на новую позицию.
def t_element(A):
    if not A:  #Проверка, пуст ли список
        return A  #Если список пуст, возвращаем его
    last_element = A[-1]  
    A = A[:-1] 
    try:
        for i in A:  
            if i > last_element:
                A.insert(A.index(i), last_element) 
                return A 
    except ValueError:
        A.append(last_element)

    A.append(last_element)
    return A

A = [1, 3, 5, 7, 9, 6] 
d_A = t_element(A)
print(d_A) 