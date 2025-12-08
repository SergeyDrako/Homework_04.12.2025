import time
def wait_with_retry_until(timeout, interval):
    def decorator (func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            my_interval=0
            сounter=1
            while my_interval <= timeout:
                if func(*args, **kwargs) is True:
                   print(f" Попытка {сounter}  успешная")
                   print('Элемент найден: ')
                   break
                else:
                    print(f" Попытка {сounter}  неуспешная")
                    сounter+=1
                    my_interval += interval
                    time.sleep(interval)
        return wrapper
    return decorator

@wait_with_retry_until(timeout=3, interval=0.5) # wait_with_retry_until=element_visible(timeout=3, interval=0.5)
def element_visible():
    return time.time() % 3 > 2  # имитация появления элемента

element_visible()
