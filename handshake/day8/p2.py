#Build BankAccount class with deposit and withdraw.
class BankAccount:
    def __init__(self, account_no, name, balance=0):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Current Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Current Balance:", self.balance)
        else:
            print("Insufficient balance")


acc = BankAccount(12345, "Ayush", 5000)


acc.deposit(2000)
acc.withdraw(3000)
acc.withdraw(5000)
