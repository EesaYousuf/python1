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