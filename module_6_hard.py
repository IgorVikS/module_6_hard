import math
class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__color = list(color)
        self.__sides = list(sides)
        self.filled = False
    def get_color(self):
        return self.__color
    def get_sides(self):
        return self.__sides
    def __is_valid_color(self, r, g, b):
        for c in [r, g, b]:
            if isinstance(c, int) and 0 <= c <= 255:
                return True
            return False
    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count:
            for side in sides:
                if isinstance(side, int) and side > 0:
                    return True
                return False
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g , b):
            self.__color = [r, g, b]
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides =list(new_sides)
    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1
    def __radius(self):
        return self.__len__ * (2/pi)
    def get_square(self):
        return (self.__len__**2)/(4*pi)
class Triangle(Figure):
    sides_count = 3
    def __height(self):
        sp = self.__len__/2
        h = (2**(sp(sp-self.__sides[0])(sp-self.__sides[1])(sp-self.__sides[2])))/2*sp
        return h
    def get_square(self):
        sp = self.__len__/2
        s = sqrt((sp(sp - self.__sides[0])(sp-self.__sides[1])(sp-self.__sides[2])))
        return s
class Cube(Figure):
    sides_count = 12
    def __init__(self, color,  *sides: int, filled: bool = True):
        super().__init__(color, *sides, filled)
        if len(sides) == 1:
            self.__sides = self.sides_count*[i for i in sides]
        else:
            self.__sides = [1*self.sides_count]
    def get_sides(self):
        return [*self.__sides]
    def get_volume(self):
        return self.__sides[1]**3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
