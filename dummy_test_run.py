def dummy_test(data):
    if data <= 5:
        return True
    else:
        return False

tests = [
(dummy_test(5), True),
(dummy_test(7), True),
(dummy_test(6), False),
(dummy_test(2), True),
(dummy_test(4), False),
(dummy_test(8), True),
(dummy_test(1), False),
]

for result, expected in tests:
    try:
        assert result == expected
    except AssertionError as e:
        print(f"Тест не пройден! Ожидается что пароль результат {expected}, " +
              f"но фактический результат {result}")
        continue
    print("Тест прошёл!")

import yaml

with open ('dummy_tests.yaml', 'w', encoding="utf-8") as file_tests:
    yaml.safe_dump(tests, file_tests, default_flow_style=False,sort_keys=False)

with open ('dummy_tests.yaml', 'r', encoding="utf-8") as file_tests:
    data_tests = yaml.safe_load(file_tests)
    # print(data_tests) # для контроля данных
    report = []
    count_failed = sum(1 for result, expected in data_tests if result == expected)
    failed_all = {'failed': count_failed}
    print(failed_all)  # Проверка данных
    report.append(failed_all)

    count_passed = sum(1 for result, expected in data_tests if result is True)
    passed_all = {'passed': count_passed}
    print(passed_all)  # Проверка данных
    report.append(passed_all)

    total = count_failed + count_passed
    total_all = {'total': total}
    print(total_all)
    report.append(total_all)

    percent = count_failed / total * 100
    percent_1 = {'Negative tests': round(percent,2)}
    print(percent_1)
    report.append(percent_1)

    percent = count_passed / total * 100
    percent_2 = {'Positive tests': round(percent, 2)}
    print(percent_2)
    report.append(percent_2)

with open ('report_test.yaml', 'w', encoding="utf-8") as file_report:
    yaml.safe_dump(report, file_report, default_flow_style=False,sort_keys=False)

