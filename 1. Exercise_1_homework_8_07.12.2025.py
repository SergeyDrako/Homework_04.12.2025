import time
def retry(times=3):
    def decorator(func):
        func()
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                result = func(*args, **kwargs)
                if result == "PASSED":
                    return result
                print(f"Попытка {attempt + 1} не удалась: {result}")
                time.sleep(1)
            return "Все попытки исчерпаны."
        return wrapper
    return decorator

@retry(times=2)
def flaky_test():
    if time.time() % 2 < 1:
        return "FAILURE"
        return "PASSED"
# flaky_test=retry(times=2)
print(flaky_test())
