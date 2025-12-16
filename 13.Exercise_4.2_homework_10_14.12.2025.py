def print_length(obj):
    print(len(obj))

print_length("Python")
print_length([1, 2, 3])
print_length({"a": 1, "b": 2})

class TestCollection:
    def __init__(self, collection):
        self.collection = collection

    def __len__(self):
        return len(self.collection)

print_length(TestCollection([10, 20, 30, 40]))
