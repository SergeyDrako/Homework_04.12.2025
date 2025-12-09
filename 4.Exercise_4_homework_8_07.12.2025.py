import time
def wait_with_retry_until(timeout, interval):
    def decorator (func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            my_interval=0
            сounter=1

            while my_interval <= timeout:
                result = func(*args, **kwargs)
                if result is True: # еслі результат выполненія функціі True
                   print(f" Попытка {сounter}  успешная")
                   print('Элемент найден: ')
                   return result
                else:
                    print(f" Попытка {сounter}  неуспешная")
                    сounter+=1
                    my_interval += interval
                    time.sleep(interval)
            print("Время ожидания истекло. Элемент не найден.")
            return None
        return wrapper
    return decorator

@wait_with_retry_until(timeout=3, interval=0.5) # wait_with_retry_until=element_visible(timeout=3, interval=0.5)
def element_visible():
    return time.time() % 3 > 2  # имитация появления элемента 0%3=остаток, 0.5%3 остаток 0.5, 1%3 остаток 1
element_visible()
