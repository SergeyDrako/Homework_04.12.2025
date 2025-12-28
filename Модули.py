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
import os

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
# 1.Exercise:Скопируйте файл settings.ini в файл settings_backup.ini в той же папке.
# with open('text_Drako_name.txt', 'w') as file:
#     file.write('Order 12, table 7, check 350.50, order in name Sergey')
#
# a = open('text_Drako_name.txt', 'r')
# print(a.read())
# a.close()
#
# with open('text_Drako_name_2.txt', 'w') as file:
#     pass
import shutil
# shutil.copy('text_Drako_name.txt', 'text_Drako_name_2.txt')

# shutil.copy2('text_Drako_name.txt', 'text_Drako_name_2.txt')
# from os import stat
# from time import ctime
#
# def file_metadata(file_name):
#     stat_into= stat(file_name)
#     print('mode:', oct(stat_into.st_mode))
#     print('Created:', ctime(stat_into.st_ctime))
#     print('Accessed:', ctime(stat_into.st_atime))
#     print('Modified:', ctime(stat_into.st_mtime))
#
# print('text_Drako_name.txt')
# file_metadata('text_Drako_name.txt')
#
# print('text_Drako_name_2.txt')
# file_metadata('text_Drako_name_2.txt')

# 2.Exercise:Скопируйте файл app.log в папку logs_backup/.
# Если директория не существует — создайте её через os.makedirs.
# import os
# logs_backup = 'logs_backup/data/raw_data'
# try:
#     os.makedirs(logs_backup, exist_ok=True)
#     print(f"Directory '{logs_backup}' ensured to exist.")
# except OSError as e:
#     print(f"Error creating directory: {e}")
#
# with open("app.log", "w") as f:
#     f.write("Hello, World!")
#     a = open('app.log', 'r')
#     # print(a.read())
#     # a.close()

import shutil
# # shutil.copy('app.log', 'logs_backup')
# # shutil.copy('app.log', 'project')
# # # 3.Exercise:Рекурсивное копирование проекта
# # Скопируйте всю папку project/ в project_backup/. Если project_backup уже существует —
# # удалите её через shutil.rmtree и затем повторите копирование.
# # shutil.copytree('logs_backup', 'logs_backup_new')
# # 4.Exercise:Переименуйте файл report.txt в report_old.txt с помощью shutil.move.
# # Если файл не найден — выведите понятное сообщение.
# # shutil.move('logs_backup_new', 'logs_backup_copy')
#
# with open("report.txt", "w") as f:
#     f.write("Hello, new WORK")
# a = open("report.txt", "r")
# print(a.read())
# a.close()
#
# try:
#     shutil.move('report.txt', 'report_old.txt')
# except(FileNotFoundError):
#     print(f"файл не найден.")

# Задание 9. Проверка свободного места на диске
# Напишите функцию, которая выводит общий объём, занятое и
# свободное место для текущего диска (путь ".") в мегабайтах.

# def calculate_memory(path):
#     disk_info = shutil.disk_usage(path)
#     toMb = lambda x: x / 1024 ** 2
#     total,used,free = list(map(toMb, disk_info))
#     print(f"Общая память {total} MB")
#     print(f"Использумая память:{used}  MB")
#     print(f"Свободная память: {free} MB")
#
# calculate_memory(r"D:")

# Задание 10. Используя shutil.which, найдите путь к интерпретатору Python ("python" или "python3").
# Выведите найденный путь, либо сообщение, что команда не найдена.
try:
    a = shutil.which("python")
    b = shutil.which("python3")
    c = shutil.which('app.log')
    print(a)
    print(b)
    print(c)
except(TypeError, NameError):
    print(f"команда не найдена.")

# Модуль datetime
# import datetime
# # 1.Exercise:Получите текущую дату и время и выведите их.
# now = datetime.datetime.now()
# print(now)
#
# 2.Exercise: Создайте объект datetime для даты вашего рождения.
# date_mybirthday = datetime.date(1990, 10, 20)
# print(date_mybirthday)
#
# 3.Exercise: Выведите год, месяц и день текущей даты отдельно.
# print(date_mybirthday.year)
# print(date_mybirthday.month)
# print(date_mybirthday.day)
# 4. Exercise:Отформатируйте текущую дату в строку формата ДД-ММ-ГГГГ.
# formatted = date_mybirthday.strftime("%d-%m-%Y")
# print(formatted)

















