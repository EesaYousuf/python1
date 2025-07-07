class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    @property
    def balance(self):
        """Getter for balance"""
        return self.__balance
