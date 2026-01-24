import xml.etree.ElementTree as ET
import random

# Данные для генерации
names = ["John", "Alex", "Maria", "David", "Elena", "Mike", "Sarah", "Tom", "Anna", "Paul"]
roles = ["QA", "AQA", "DEV", "PM", "PO", "CEO", "HR", "Senior QA", "Junior DEV", "Team Lead"]

# Создание корневого элемента
root = ET.Element('company')
root.set('name', 'TechCorp')
root.set('generated', '2026-01-14')

# Генерация 10 пользователей
for i in range(10):
    user = ET.SubElement(root, 'employee', {'id': str(i + 1)})

    name_elem = ET.SubElement(user, 'name')
    name_elem.text = random.choice(names)

    role_elem = ET.SubElement(user, 'role')
    role_elem.text = random.choice(roles)

    salary_elem = ET.SubElement(user, 'salary')
    salary_elem.text = str(random.randint(1000, 10000))


tree = ET.ElementTree(root)
tree.write('employees.xml', encoding='utf-8', xml_declaration=True)

tree = ET.parse('employees.xml')
root = tree.getroot()

all_employee = []
all_salary = []
for employee in root.findall('employee'):
    one_employee = employee.find('name').text
    every_salary = employee.find('salary').text
    id_each = employee.get('id')

    all_salary.append(int(every_salary))
    all_employee.append(one_employee)
    print(f"ID: {id_each}, Name:{one_employee}, Salary: {every_salary}")

sum_salary = sum(all_salary)
print(f"Сумма заработных плат: {sum_salary} $")

count_employee = len(all_employee)
print(f'Количество сотрудников: {count_employee}')









