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
        # --- Derived Class ---
class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.03):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"Interest of {interest:.2f} applied.")
        # --- Another Derived Class ---
class CheckingAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=100):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self._balance + self.overdraft_limit:
            raise InsufficientFundsError("Overdraft limit exceeded!")
        self._balance -= amount
        print(f"{amount} withdrawn from {self.owner}'s checking account.")
# --- Demo Usage ---
if __name__ == "__main__":
    alice = SavingsAccount("Alice", 1000)
    bob = CheckingAccount("Bob", 500)

    alice.deposit(200)
    alice.apply_interest()
    print(alice.get_account_info())

    bob.withdraw(550)
    try:
        bob.withdraw(100)
    except InsufficientFundsError as e:
        print("Error:", e)

    print(bob.get_account_info())