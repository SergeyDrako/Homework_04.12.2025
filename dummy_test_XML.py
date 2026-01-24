import xml.etree.ElementTree as ET

from pyexpat.errors import messages


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
failed_count = 0
passed_count = 0
list_error = []

for result, expected in tests:
    try:
        assert result == expected
        passed_count += 1
    except AssertionError as e:
        failed_count += 1
        message = f"Тест не пройден! Ожидается что пароль результат {expected}, но фактический результат {result}"
        list_error.append(message)
        print(message)
        continue
    print("Тест прошёл!")

print(passed_count)
print(failed_count)

total = passed_count + failed_count

root = ET.Element('report')
root.set('generated', '2026-01-19')

total = ET.SubElement(root, 'total', {'total': str(total)})

passed = ET.SubElement(root, 'passed', {'passed': str(passed_count)})

failed = ET.SubElement(root, 'failed', {'failed': str(failed_count)})

for error in list_error:
    ET.SubElement(failed, 'error',{'error': error})




tree = ET.ElementTree(root)
tree.write('Test_report.xml', encoding='utf-8', xml_declaration=True)










