class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # public
        self._balance = balance     # protected (internal use)
        self.__account_number = "123ABC456"  # private

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self.__account_number  # exposing private attribute via method
        # --- Testing Encapsulation ---
account = BankAccount("Alice", 1000)

print(account.owner)          # ✅ Public: Accessible
print(account._balance)       # ⚠️ Protected: Accessible but not recommended

try:
    print(account.__account_number)  # ❌ Private: AttributeError
except AttributeError as e:
    print("Error:", e)
# ✅ Correct way to access private data:
print(account.get_account_number())

# 🔍 But private variables still exist...
print(account._BankAccount__account_number)  # ⚠️ Name-mangled access (hacky)
