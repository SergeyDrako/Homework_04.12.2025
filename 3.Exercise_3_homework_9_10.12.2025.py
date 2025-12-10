class Shape:
    def area(self):
        print()

    def print_info(self):
        print(f" Площадь: {self.area()}")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area (self):
            return self.width * self.height

Rectangle_1 = Rectangle(30, 50)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area (self):
        return 3.14 * (self.radius ** 2)

Circle_1 = Circle(10)

Rectangle_1.print_info()
Circle_1.print_info()
# print(Rectangle_1.area())
# print(Circle_1.area())


