from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.__balance = float(balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance

    @abstractmethod
    def account_type(self):
        pass

    def __str__(self):
        return f"{self.account_type()} account for {self.owner}: ${self.__balance:.2f}"


class SavingsAccount(Account):
    def account_type(self):
        return "Savings"

    def withdraw(self, amount):
        if amount > 1000:
            raise ValueError("Cannot withdraw more than 1000 from savings at once")
        return super().withdraw(amount)


class CheckingAccount(Account):
    def account_type(self):
        return "Checking"

    def withdraw(self, amount):
        return super().withdraw(amount)


if __name__ == "__main__":
    savings = SavingsAccount("Alex", 1500)
    checking = CheckingAccount("Alex", 500)

    savings.deposit(200)
    checking.deposit(100)

    try:
        savings.withdraw(1200)
    except ValueError as error:
        print(error)

    checking.withdraw(250)

    print(savings)
    print(checking)
    print("Savings balance:", savings.get_balance())
    print("Checking balance:", checking.get_balance())