import uuid

# --- Custom Exception ---
class InsufficientFundsError(Exception):
    pass
# --- Base Class ---
class Account:
    bank_name = "GPT National Bank"  # class variable shared by all instances

    def __init__(self, owner, balance=0):
        self.__account_number = str(uuid.uuid4())[:8]  # private attribute
        self.owner = owner
        self._balance = balance  # protected attribute
        def deposit(self, amount):
        self._balance += amount
        print(f"{amount} deposited to {self.owner}'s account.")

    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFundsError("Insufficient funds!")
        self._balance -= amount
        print(f"{amount} withdrawn from {self.owner}'s account.")

     def get_balance(self):
        return self._balance

    def get_account_info(self):
        return {
            "Owner": self.owner,
            "Account Number": self.__account_number,
            "Balance": self._balance
        }