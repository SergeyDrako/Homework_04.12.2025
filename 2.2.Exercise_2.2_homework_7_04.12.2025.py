tests = [
    {"name": "complex_test", "duration": 5.2},
    {"name": "simple_test", "duration": 1.1},
    {"name": "medium_test", "duration": 3.4}
]

tests.sort(key=lambda test: test['duration'])

print(tests)

