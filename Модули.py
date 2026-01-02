# Модуль math
# #1.Exercise:Вычислите площадь круга с радиусом 7 (используйте math.pi и pow
# import math
#
# # a = (math.pow(7,2))
# # b = (math.pi)
# # Area_circle = a*b
# # print(Area_circle)
#
# #2.Exercise:Найдите наибольшее целое число, не превышающее число 9.8 (используйте math.floor()).
# # print(math.floor(9.8))
#
# #3.Exercise:Рассчитайте значение синуса 45 градусов (переведите градусы в радианы).
# # print(math.sin(math.radians(45)))
#
# #4.Exercise:4.	Выведите квадратный корень из числа 144.
# # print(math.sqrt(144))
#
# #5.Exercise:5.	Найдите наибольший общий делитель чисел 270 и 192.
# # print(math.gcd(270,192))
#
# #6.Exercise:6.Используя math.exp(), вычислите значение e в степени 3.
# # print(math.exp(3))
#
# #7.Exercise:7.Найдите факториал числа 8
#
# #8.Exercise:8.Определите степень, в которую нужно возвести 2, чтобы получить 256 (используйте math.log()).
# # print(math.log(256,2))
#
# #9.Exercise:9. 9.Округлите число 3.14159 до ближайшего целого с помощью math.ceil().
# # print(math.ceil(3.14159))???
#
# #10.Exercise:10.Напишите функцию, которая принимает угол в градусах и возвращает тангенс этого угла.
#
# def tangents(degrees):
#     radians =math.radians(degrees)
#     tangent = math.tan(radians)
#     return tangent
#
# # tangents(45)
# # print(tangents(45))
# a = 45
# resultat = tangents(a)
# print(resultat)

# Модуль random
# import random
# n = random.randint(1, 6)
# print(n)
# n = random.randrange(0, 10, 2)
# print(n)
# colors = ["red", "green", "blue"]
# c = random.choice(colors)
# print(c)
# lottery = [1, 2, 3, 4, 5, 6]
# nums = random.choices(lottery, k=5)
# print(nums)
# deck = [1, 2, 3, 4, 5]
# random.shuffle(deck)
# 1.Exercise:1. Смоделируйте бросок шестигранного кубика и выведите результат.
# x = random.randint(1,6)
# print(x)

# 2.Exercise:2. Случайный пароль из букв
# a = 'abcdefghijklmnopqrstuvwxyz'
# password = random.choices(a, k=8)
# print(password)
#
# password_1 = random.sample(a, k=8)
# print(password_1)
# 3.Exercise:3. Есть список методов HTTP: ["GET", "POST", "PUT", "DELETE"].
# Напишите функцию, которая случайно выбирает один метод.

# def random_email():
#     HTTP = ["GET", "POST", "PUT", "DELETE"]
#     return random.choice(HTTP)
#
# a = random_email()
# print(a)

# Модуль shutil
with open('text_Drako_name.txt', 'w') as file:
    file.write('Order 12, table 7, 350.50, order in name Sergey')

a = open('text_Drako_name.txt', 'r')
print(a.read())
a.close()


# import shutil
# # hutil.copy('text_Drako_name.txt', 'text_Drako_name_2.txt')
# shutil.copy2('text_Drako_name.txt', 'text_Drako_name_2.txt')
#
#
# # 1.Exercise: Скопируйте файл settings.ini в файл settings_backup.ini в той же папке.
# shutil.copy("settings.ini", "settings_backup.ini")
# os.makedirs('my_fail/settings.ini', exist_ok=True)
# with open('my_fail/settings_backup.ini, 'w') as f:
#     f.write('Hello World!')



# #Модуль datetime
# import datetime
#
# # 1.Exercise:Получите текущую дату и время и выведите их.
# # now = datetime.datetime.now()
# # 2.Exercise: Создайте объект datetime для даты вашего рождения.
# date_mybirthday = datetime.date(1990, 10, 20)
# print(date_mybirthday)
# # 3.Exercise: Выведите год, месяц и день текущей даты отдельно.
# print(date_mybirthday.year)
# #4. Exercise:Отформатируйте текущую дату в строку формата ДД-ММ-ГГГГ.
# formatted = date_mybirthday.strftime("%d-%m-%Y")
# print(formatted)

















