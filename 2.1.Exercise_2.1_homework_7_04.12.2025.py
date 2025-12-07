test_results = [
    {"name": "login_test", "status": "passed", "duration": 2.1},
    {"name": "payment_test", "status": "failed", "duration": 3.5},
    {"name": "logout_test", "status": "passed", "duration": 1.2}
]

good_test = list(filter(lambda tests: tests["status"]=='passed',test_results))
print(good_test)
