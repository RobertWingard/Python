class BankAccount:
        # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        print(f'This is your new balance after deposit: {self.balance}')
        return self
    def withdraw(self, amount):
        self.balance -= amount
        print(f'This is your new balace after your withdraw: {self.balance}')
        return self
    def display_account_info(self):
        print(f'Interest Rate: {self.int_rate}')
        print(f'Balance: {self.balance}')
        return self
    def yield_interest(self):
        rate = self.balance * self.int_rate
        self.balance += rate
        return self




account1 = BankAccount(.02, 100)
account2 = BankAccount(.02, 100)


account1.deposit(10).deposit(15).deposit(20).withdraw(5).yield_interest().display_account_info()


account2.deposit(10).deposit(15).withdraw(5).withdraw(5).withdraw(10).withdraw(5).yield_interest().display_account_info()

