from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def total(self):
        return self.price * self.quantity

    def __add__(self, other):
        return Product(self.name, self.price, self.quantity + other.quantity)

p1 = Product("Keyboard", 50.0, 2)
p2 = Product("Mouse", 25.0, 1)
p3 = p1 + p2

print(p1.total())
print(p2.total())
print(p3.total())


