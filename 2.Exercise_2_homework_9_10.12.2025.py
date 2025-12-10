class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def print_info(self):
        print(f" Имя работника: {self.name}, доход работника: {self.salary}")
# Employee_1 = Employee("John", 80000)
# Employee_2 = Employee ("Victor", 30000)
# # print(Employee_1.name, Employee_1.salary)
# # print(Employee_2.name, Employee_2.salary)

class Manager(Employee):
    def __init__ (self, name, salary=10):
        Employee.__init__(self, name, salary) # альтернотивный super().__init__(name, salary)
        # print(self.name, self.salary)

class Developer(Employee):

    def __init__ (self, name, salary=500):
        Employee.__init__(self, name, salary)
        # print(self.name, self.salary)
manager_1 = Manager("John")
Developer_1 = Developer("Victor")
manager_1.print_info()
Developer_1.print_info()
