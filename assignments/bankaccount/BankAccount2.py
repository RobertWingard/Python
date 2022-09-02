class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount, name):
        self.balance += amount
        print(f'{name} this is your new balance after deposit: {self.balance}')
        return self

    def withdraw(self, amount, name):
        self.balance -= amount
        print(f'{name} this is your new balace after your withdraw: {self.balance}')
        return self

    def display_account_info(self, name):
        print(f"{name} this is your interest Rate: {self.int_rate}")
        print(f"{name}'s Current balance: {self.balance}")
        return self

    def yield_interest(self):
        rate = self.balance * self.int_rate
        self.balance += rate
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {'checking': BankAccount(int_rate=0.02, balance=0), 'savings': BankAccount(int_rate=0.02, balance=0)}

    def make_deposit(self, amount, account_name):
        self.account[account_name].deposit(amount, self.name)
        return self

    def make_withdraw(self, amount, account_name):
        self.account[account_name].withdraw(amount, self.name)
        return self

    def display_user_balance(self):
        self.account.display_account_info(self.name)
        return self


user_1 = User('Robert', 'email.com')
user_2 = User('Chris', 'email.com')


user_1.make_deposit(10, 'checking')

user_1.account['checking'].deposit(10, 'Robert')
print('==============') # line between just because
user_2.account['savings'].deposit(20, 'Chris')







# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

# SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.

