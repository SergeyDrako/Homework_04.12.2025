class Account:
    def __init__ (self, balance=0):
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

class SavingsAccount(Account):
    interest_rate = 0.05
    def add_interest(self):
       # self.balance += self.balance * self.interest_rate
       self.deposit( self.balance * self.interest_rate)
account = SavingsAccount(1000)
account.deposit(500)      # Работает метод родителя
account.add_interest()
print(account.balance)    # 1575.0
