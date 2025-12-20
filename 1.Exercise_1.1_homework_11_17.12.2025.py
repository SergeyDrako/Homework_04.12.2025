def test_info(author, component):
    def decorator(cls):
        cls.author = author
        cls.component = component
        return cls
    return decorator

@test_info(author="Иван", component="Auth")
class TestLogin:
    pass

print(TestLogin.author)
print(TestLogin.component)


