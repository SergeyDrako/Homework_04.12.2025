class LoggingMixin:
    def log(self):
        print(f"LOG Выполняем задачу")

class RetryMixin:
    def retry(self, count):
        for i in range(1,count+1):
            print(f"номер попыткі {i}")
            self.run()

class Job(LoggingMixin,RetryMixin):
    def run(self):
        self.log()
        print("что-то делает")

j = Job()
j.retry(2)


