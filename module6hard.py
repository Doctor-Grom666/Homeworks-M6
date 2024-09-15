import math


class Figure:
    sides_count = 0
    filled = bool

    def __init__(self, __color, *__sides):
        self.__color = [*__color]
        if len(__sides) == self.sides_count:
            self.__sides = [*__sides]

    # @property
    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        if 0 <= (r or g or b) <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        valid = True
        for i in args:
            if not isinstance(i, int) or len(args) != self.sides_count:
                valid = False
        return valid

    # @property
    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = [*new_sides]

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __radius(self):
        return round((self.get_sides()[0] / 6.28), 2)

    def get_square(self):
        return round((3.14 * (self.__radius() * self.__radius())), 2)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        sides = self.get_sides()
        p = 0.5 * sum(sides)
        s = round(math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])), 2)
        return s


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, __sides: int):
        super().__init__(__color)
        self.__sides = [__sides] * self.sides_count

    # @property
    def get_sides(self):
        return self.__sides

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((150, 67, 200), 5, 7, 4)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка площади круга
print(circle1.get_square())

# Проверка площади треугольника
print(triangle1.get_square())
