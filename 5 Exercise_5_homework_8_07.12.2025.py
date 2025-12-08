import time
# results={}
def cache_results(results):
    def decorator (func):
        def wrapper(*args, **kwargs):
            if args[0] not in results:
                results[args[0]] = func(*args, **kwargs)
            return results[args[0]]
        return wrapper
    return decorator

@cache_results({}) # expensive_calculation=cache_results(expensive_calculation)
def expensive_calculation(n):
    print(f"Вычисляем для {n}")
    time.sleep(1)
    return n * n

print(expensive_calculation(5)) #медленно считает
print(expensive_calculation(5)) #быстро возвращает из кеша
print(expensive_calculation(5)) #быстро возвращает из кеша
print(expensive_calculation(6)) #медленно считает
print(expensive_calculation(5)) #быстро возвращает из кеша