from abc import ABC, abstractmethod
class Transport:
    @abstractmethod
    def move (self):
        pass
    def go(self):
        print('Начинаем движение')
        self.move()

class Car(Transport):
        def move(self):
            print('Едем по дороге на машине')


class Bike(Transport):
       def move(self):
            print('Едем на велосипеде')
            

for t in (Car(), Bike()):
        t.go()



