# Create a User class with an __init__ method

# Add a make_deposit method to the User class that calls on
# it's bank account's instance methods.

# Add a make_withdrawal method to the User class that calls
# on it's bank account's instance methods.

# Add a display_user_balance method to the User class that
# displays user's account balance

# SENSEI BONUS: Allow a user to have multiple accounts; update
# methods so the user has to specify which account they are
# withdrawing or depositing to

# SENPAI BONUS: Add a transfer_money(self, amount, other_user)
# method to the user class that takes an amount and a different
# User instance, and transfers money from the user's account
# into another user's account.

class BankAccount:

    accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        self.account2 = BankAccount(int_rate=.07, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(self.name)
        self.account.display_account_info()
        return self

ah1 = User("Donald", "bigdaddy24@hotmail.com")
ah1.make_deposit(100).make_deposit(250).display_user_balance()

ah2 = User("Mary", "MaryPoppins@gmail.com")
ah2.make_deposit(1000).display_user_balance().make_withdraw(450).display_user_balance()

