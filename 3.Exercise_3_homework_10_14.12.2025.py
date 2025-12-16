class TestStats:
    def __init__(self, passed, total):
        self.passed = passed
        self.total = total

    @property
    def success_rate(self):
        return self.passed / self.total* 100

stats = TestStats(8, 10)
print(stats.success_rate)
stats.passed = 9
print(stats.success_rate)






