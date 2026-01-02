def generate_report(title, *test_names, format="html", **options):
    print('Отчет:',title)
    print('Тесты: ', test_names)
    print('Формат: ', format)
    print('Разное:', options)
generate_report("Daily Report", "test1", "test2", "test3", format="pdf", author="Tester", word="good")
