# class Temperature:
#     def __init__(self, celsius):
#         self._celsius = celsius # Скрытый атрибут
#
#     @property # Геттер
#     def celsius(self):
#         return self._celsius
#
#     @celsius.setter # Сеттер
#     def celsius(self, value):
#         if value < -273.15:
#             raise ValueError("Температура не может быть ниже абсолютного нуля")
#         self._celsius = value # Логика установки значения
#
# # Использование:
# temp = Temperature(20)
# print(temp.celsius) # Вызов геттера: 20
#
# temp.celsius = 35 # Вызов сеттера: установка нового значения
# print(temp._celsius)

class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self.__price = new_price

# # Использование:
gift = Product(100)
print(gift.price)
gift.price = 250  # вызов сеттера: установка нового значения
print(gift.price)
gift.price = -10
print(gift.price)













