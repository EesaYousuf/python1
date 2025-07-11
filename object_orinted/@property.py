class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    @property
    def balance(self):
        """Getter for balance"""
        return self.__balance
@property
    def balance(self):
        """Getter for balance"""
        return self.__balance

    @balance.setter
    def balance(self, amount):
        """Setter with validation"""
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = amount

    @property
    def is_premium(self):
        """Read-only computed property"""
        return self.__balance >= 10000
# --- Usage ---
account = BankAccount("Alice", 5000)

# ✅ Get balance (calls getter)
print(account.balance)

# ✅ Set balance (calls setter with validation)
account.balance = 8000
print(account.balance)
# ❌ Attempt to set invalid balance
try:
    account.balance = -1000
except ValueError as e:
    print("Error:", e)

# ✅ Read-only computed property
print("Is Premium:", account.is_premium)

# ❌ Cannot set read-only property
try:
    account.is_premium = False
except AttributeError as e:
    print("Error:", e)
