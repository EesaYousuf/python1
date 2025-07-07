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
