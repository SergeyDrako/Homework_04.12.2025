class Vehicle:
    def __init__(self, move):
        self.move = int(move)
    def move_1(self, perfect):
        self.move = self.move + perfect
        print(f"Машина едет со скорость {perfect}км/ч.")
Vehicle_1 = Vehicle('50')
Vehicle_1.move_1(30)
print(f"Моя машина едет быстрее {Vehicle_1.move}км/ч.")

class Car(Vehicle):
    def honk(self):
        print("БИП-БИП")
car = Car(100)
car.move_1(5)
print(f"Самая быстрая машина на дороге:  {car.move}")
car.honk()   # БИП-БИП!

# class Vehicle:
#     def __init__(self, name):
#         self.name = name
#
#     def move(self, move):
#         print(f"{self.name} is moving.")
#
# class Car(Vehicle):
#     def honk(self):
#         print("БИП-БИП!")
#
# Vehicle_1 = Vehicle()
# Vehicle_1.move()
#
# car = Car(100)
# car.move()
# car.honk()

