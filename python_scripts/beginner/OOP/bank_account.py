class BankAccount:
    def __init__(self, owner, balance=float(0)):
        self.owner = owner
        self.balance = balance

    def deposit(self, num):
        self.balance += num
        return self.balance

    def withdraw(self, num):
        self.balance -= num
        return self.balance

acct = BankAccount("Darcy")
print(acct.owner)
print(acct.balance)
print(acct.deposit(10))
print(acct.withdraw(3))
print(acct.balance)