from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return 3.14 * self._radius * self._radius

# def main(parameter:Shape):
#     print(parameter.area())
# rectangle = Rectangle(3, 4)
# circle = Circle(2)
# main(rectangle)
# main (circle)

# rectangle = Rectangle(3, 4)
# circle = Circle(2)
# shapes = [rectangle, circle]
# shapes = [Rectangle(3, 4), Circle(2)]
# for s in shapes:
#     print(s.area())