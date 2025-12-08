import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() # Запоминаем время начала выполнения
        result = func(*args, **kwargs) # Вызываем оригинальную функцию
        end_time = time.time() # Запоминаем время окончания выполнения
        finsh_time = end_time - start_time #  Вычисляем время выполнения

        print(f"Функция {func()} выполнена {finsh_time: } секунду")
        return result # # Возвращаем результат выполнения функции
    return wrapper

@timer
def slow_test():
    time.sleep(1)
    return "ОК"


slow_test()