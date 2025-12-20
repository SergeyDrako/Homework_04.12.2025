from enum import Enum

class Priority(Enum):
    HIGH = 1
    LOW = 2
    MEDIUM = 3

tasks = [
    ("Починить тест логина", Priority.HIGH),
    ("Обновить документацию", Priority.LOW),
    ("Настроить CI", Priority.MEDIUM),
]

tasks_sorted = sorted(tasks, key = lambda task: task[1].value)
print(tasks_sorted)

def filter_tasks(tasks):
    for name, priority in tasks_sorted:
        print(priority.name, "-", name)

filter_tasks(tasks_sorted)

print(type(tasks_sorted))


