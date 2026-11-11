from math import pi

class Figure:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def __str__(self):
        return f"{self.name}: площадь {self.area():.2f}"

class Rect(Figure):
    def __init__(self, width, height):
        super().__init__("Прямоугольник")
        self.width, self.height = width, height

    def area(self):
        return self.width * self.height

class Circle(Figure):
    def __init__(self, radius):
        super().__init__("Круг")
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

figures = [Rect(4, 5), Circle(3), Rect(2, 7)]
total = 0
for figure in figures:
    print(figure)
    total += figure.area()
print(f"Всего: {total:.2f}")
