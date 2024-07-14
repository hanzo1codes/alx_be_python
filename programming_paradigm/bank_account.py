# bank_account.py

class BankAccount:
    """A simple bank account class."""

    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw a specified amount from the account if sufficient funds are available."""
        if amount > self.account_balance:
            return False
        self.account_balance -= amount
        return True

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")
