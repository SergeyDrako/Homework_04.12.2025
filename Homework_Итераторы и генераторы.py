# 1. Exercise:
# Написать генератор even_numbers(iterable),
# который принимает итерируемый объект и выдаёт только чётные числа.
# def even_numbers(iterable):
#     for item in iterable:
#         if item % 2 == 0:
#             yield item
#
# print(list(even_numbers([1, 2, 3, 4, 5, 6])))
# print(type(even_numbers([1, 2, 3, 4, 5, 6])))

# 2. Exercise:
# На основе read_lines(path) написать генератор filter_lines(path, keyword),
# # который выдаёт только строки, содержащие keyword.
# def filter_lines(path, keyword):
#     with open(path) as file:
#         for line in file:
#             if keyword in line:
#                 yield line
#
# with open('log.txt', 'w') as file:
#     file.write('Hello, world!ERROR. python os the best!')
# a = open('log.txt', 'r')
# print(a.read())
#
# for line in filter_lines("log.txt", "ERROR"):
#     print(line)
# 3. Exercise: Написать генератор chain(iter1, iter2), который последовательно выдаёт элементы сначала из iter1,
# затем из iter2 (аналог itertools.chain, но вручную).
# Дополнительная информация: yield в генераторе может быть сколько угодно,
# при следующем вызове генератор продолжает работать с того yield на котором остановился.
# def chain(iter1, iter2):
#     for num1 in iter1:
#         yield num1
#     for num2 in iter2:
#         yield num2
#
# print(list(chain([1, 2], [3, 4])))

# 4. Exercise: Создать генератор counter(start=0),
# который бесконечно считает: start, start+1, start+2, ...
# def counter(start=0):
#     count = start
#     while True:
#     # while count > 0: # Уточнить! Какой вариант более валидный и правльно работает*
#         yield count
#         count += 1
#
# c = counter(10)
# print(next(c))
# print(next(c))
# print(next(c))

# 5. Exercise:Используя counter, написать генератор take(n, iterable),
# который берёт только первые n элементов из любого итератора/генератора.
# Дополнительная информация:
# def take(n, iterable):
#     for i in range(n):
#         yield next (iterable)
#
# def counter(start=0):
#     count = start
#     while True:
#         yield count
#         count += 1
#
# c = counter(100)
# print(list(take(5, c)))

# 6. Exercise:Замена всех пробелов на запятые
# Дана строка "one two three\tfour".
# Нужно заменить любые последовательности пробельных символов одним символом ",".
#
# def find_word(change):
#     words = change.split()
#     resultat = ",".join(words)
#     yield resultat
#
# res = "one two three four"
#
# for word in find_word(res):
#     print(word)
# "Решение задачи с модулем re"
# import re
# res = "one two three four"
# text = re.sub(r'\s', ',',res)
# print(text)

# 7. Exercise: Дан список:
# emails = ["a@test.com", "b@mail.ru", "user@sub.example.org"]
# Нужно получить список доменов: ['test.com', 'mail.ru', 'sub.example.org'].

# import re
# domains = ["a@test.com", "b@mail.ru", "user@sub.example.org"]
# def find_domen(emails):
#     return [re.findall(r"(?:@)(.+$)", email)[0] for email in emails]
# print(find_domen(domains))

# a = re.split(r"@","a@test.com") # Тест работы кода с split
# print(a)

# email = "b@mail.ru"
# find = re.findall(r"(?:@)(.+$)", email) # Тест работы кода с findall
# print(find)

# 8 Exercise:
# Написать функцию, которая проверяет, что строка соответствует
# формату YYYY-MM-DD, где год — 4 цифры, месяц и день — по 2 цифры.
# import re
# data_1 = "2025-12-23"
# data_2 = "25-12-23"
# def check_str(data):
#     c = re.search(r"^\d{4}-\d{2}-\d{2}$", data)
#     if c is not None:
#         return True
# print(check_str(data_1))
# print(check_str(data_2))

# Решение с тестом. Проверяет наши условия.
# date_1 = "2025-12-23"
# date_2 = "25-12-23"
# def is_valid_str(data):
#     c = re.search(r"\d{4}-?:?\d{2}-?:?\d{2}", data)
#     if c is not None:
#         return True
# print(is_valid_str(date_1))
# print(is_valid_str(date_2))

# assert is_valid_str(date_1)
# assert not is_valid_str(date_2)

# 9 Exercise:
# Есть строка лога:
# log = '127.0.0.1 - - "GET /api/v1/users HTTP/1.1" 200 123 "-"'
# Нужно извлечь код ответа (200) как строку.
# import re
# log = '127.0.0.1 - - "GET /api/v1/users HTTP/1.1" 200 123 "-"'
# d = re.search(r'\s(\d{3})\s', log)
# if d:
#     print(d.group(1))
# else:
#     print("Нужен дополнительный запрос")

# 10 Exercise:
# Написать функцию, которая проверяет пароль по правилам:
# длина минимум 8 символов;
# есть хотя бы одна заглавная буква;
# есть хотя бы одна цифра.
# (?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,12}$ пробный варіант, но вроде бы работает
# password_1 = "Abcdef12"
# password_2 = "abcdef12"
# password_3 = "Abcdefgh"
# def is_valid_password(password):
#     is_valid_length = len(password) >= 8
#     has_capital = re.search(r"[A-Z]", password)
#     has_number = re.search(r"[0-9]", password)
#     if has_capital and has_number and is_valid_length:
#         return True
#     else:
#         return False
# # assert is_valid_password(password_1)
# # assert not is_valid_password(password_2)
# # assert not is_valid_password(password_3)
# print(is_valid_password(password_1))
# print(is_valid_password(password_2))
# print(is_valid_password(password_3))

# #11 Exercise:
# # Дана строка "<p>Hello <b>world</b>!</p>".
# # Нужно удалить все теги, оставив только текст: "Hello world!".
# import re
# origin_str = "<p>Hello <b>world</b>!</p>"
# html_safe_str = re.sub(r"</?\w+>" ,'', origin_str) # Вариант №1
# html_safe_str = re.sub(r"</?[pb]>" ,'', origin_str) # Вариант №2
# print(html_safe_str)

# 12 Exercise:
# Получить все пары ключ=значение
# Условие.Дана строка:
# import re
# s = "name=John; age=30; city=London;"
# Нужно получить словарь {"name": "John", "age": "30", "city": "London"}.
# s = "name=John; age=30; city=London"
# men_data = re.findall(r"(\w+)=(\w+)", s)
# dict_men_data = dict(men_data)
# print(dict_men_data)
# print(type(dict_men_data))

# 13 Exercise:
# Вытащить номер телефона
# Условие.В строке могут быть телефоны формата +7-999-123-45-67 или 8 (999) 123-45-67.
# Нужно написать функцию, которая возвращает все телефоны из строки.
# import re
# text = "Мой телефон: +7-999-123-45-67, офис: 8 (812) 555-66-77."
# find_phones = re.findall(r"\+?\d[\s-]\(?\d{3}\)?[\s-]\d{3}[-\s]\d{2}[-\s]\d{2}", text)
# print(find_phones)
# 14 Exercise: Разбить строку по нескольким разделителям.
# Разбить "one,two;three four" на слова, используя разделители ,, ; и пробелы.
# import re
# word_str = "one,two;three four"
# d = re.split(r"[,; ]", word_str)
# d_1 = re.sub(r'[,; ]', ' , ', word_str)
# print(d)
# print(d_1)
# 15 Exercise: Извлечь данные из URL.
# Из URL вида /api/v1/users/123/orders/456 извлечь user_id и order_id как числа.
import re
url = '/api/v1/users/123/orders/456'
url_int = re.findall(r"/(\d+)/?", url)
print(tuple(url_int))








