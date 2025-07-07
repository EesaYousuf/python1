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
