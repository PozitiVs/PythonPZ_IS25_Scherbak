#Создайте базовый класс "Фигура" со свойствами "ширина" и "высота". 
#От этого класса унаследуйте классы "Прямоугольник" и "Квадрат".
#Для класса "Квадрат" переопределите методы, связанные с вычислением площади периметра
class Figure:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Pram(Figure):
    pass 

class Kvad(Figure):
    def __init__(self, leng):
        super().__init__(leng, leng) 

    def area(self):
        return self.width * self.width

    def perimeter(self):
        return 4 * self.width


pr = Pram(3, 4)
print(f"Прямоугольник: Площадь = {pr.area()}, Периметр = {pr.perimeter()}")

kv = Kvad(5)
print(f"Квадрат: Площадь = {kv.area()}, Периметр = {kv.perimeter()}")