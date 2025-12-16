class TestRunner:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self):
        for clean in self.phone:
            print(f"- {clean}")

runner = TestRunner(["test_login", "test_signup", "test_payment"])
runner()
        
