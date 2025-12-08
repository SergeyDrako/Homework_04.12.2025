def required_role(required_role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if args[0] == required_role:
                print("Admin")
                return func(*args, **kwargs)
            else:
                print(f"Требуется роль {required_role}, текущая роль: {args}")
                return None # # Возврат None, если роль не соответствует
        return wrapper
    return decorator

@required_role("admin") # ("admin") # test=require_role("admin")
def test(*args):
    print("Выполняется админский тест")
    return "Success"

print(test('admin'))