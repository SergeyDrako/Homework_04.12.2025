class TestResults:
    def __init__(self):
        self._data = {}

    def __setitem__(self, key, value):
        self._data[key] = value

    def __getitem__(self, key):
        return self._data[key]

    def __len__(self):
        return len(self._data)

results = TestResults()
results["test_login"] = "passed"
results["test_payment"] = "failed"

print(results["test_login"])

print(len(results))




