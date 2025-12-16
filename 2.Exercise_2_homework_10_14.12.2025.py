class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

rect = Rectangle(3, 4)
print(rect.area)
rect.width = 10
print(rect.area)




