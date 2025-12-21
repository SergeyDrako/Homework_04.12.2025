def transform_tests(tests, transform_func):
    return list(map(transform_func, tests))

tests = [
    {"name": "test1", "duration": 2.0},
    {"name": "test2", "duration": 3.0},
    {"name": "test3", "duration": 1.5}
]

increased_tests = transform_tests(tests, lambda t:{**t, "duration": t["duration"] * 1.1})
print(increased_tests)