class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        print(f"Account Holder: {self.account}")
        print(f"Current Balance is: {self.balance}")

# Create a BankAccount object
my_account = BankAccount("John Doe", 1000)

# Perform some actions
my_account.deposit(5000)
my_account.withdraw(6000)
my_account.display_balance()
