#Дан целочисленный список размера N. 
#Увеличить все нечетные числа, содержащиеся в списке, на исходное значение последнего нечетного числа. 
#Если нечетные числа в списке отсутствуют, то оставить список без изменений.
def ase_odd(nums):
    try:
        odd_numb = []
        for num in nums:
            if num % 2 != 0:
                odd_numb.append(num)
        if not odd_numb:
            return nums
        
        last_odd = odd_numb[-1]
        result = []
        for num in nums:
            result.append(num + last_odd if num % 2 != 0 else num) 
        return result
    
    except Exception as e:
        print(f"Ошибка: {e}")
        return []

numbers = [2, 3, 4, 5, 6, 7]
result = ase_odd(numbers)
print(result)  