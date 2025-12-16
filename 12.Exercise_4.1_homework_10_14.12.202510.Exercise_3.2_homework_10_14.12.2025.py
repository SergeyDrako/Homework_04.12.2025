class  BaseTest:
    def __init__(self, page):
         self.page = page

    def run(self):
        print(f"API тест: проверяем эндпоинт {self.page}")

class APITest:
    def __init__(self, page):
        self.page = page

    def run(self):
        print(f"UI тест: проверяем страницу  {self.page}")

class UITest:
    def __init__(self, page):
        self.page = page
    def run(self):
        print(f"API тест: проверяем эндпоинт {self.page}")
tests = [
    APITest("/login"),
    UITest("LoginPage"),
    APITest("/users"),
]

def run_all(test_cases):
    for test in test_cases:
        test.run()

run_all(tests)
