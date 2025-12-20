from dataclasses import dataclass
@dataclass
class Point:
    x: float
    y: float

    def point_cata(self):
        return self.x, self.y

#     def __init__(self,x: float, y: float):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"Point(x={self.x}, y={self.y})"

p1 = Point(1.0, 2.0)
p2 = Point(-3.5, 4.2)

print(p1)  # Point(x=1.0, y=2.0)
print(p2)  # Point(x=-3.5, y=4.2)

