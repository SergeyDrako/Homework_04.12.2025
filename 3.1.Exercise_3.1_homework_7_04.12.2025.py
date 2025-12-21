def apply_test_check(check_func, test_results):
    counter = 0
    for result in test_results:
        if check_func(result):
            counter += 1
    return counter
test_results = [
    {"status": "passed"}, {"status": "failed"}, {"status": "passed"}
]
result = apply_test_check(lambda x: x['status']=='passed', test_results)
print(f"Прошло тестов: {result}")