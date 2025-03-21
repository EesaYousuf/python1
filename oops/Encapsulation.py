class BankAccount:
    def __init__(self,balance):
          self._balance=balance
    def deposit(self,amout):
         self._balance+=amout
    def get_balnace(self):
         return self._balance
account=BankAccount(1000)
account.deposit(600)
print(account.get_balnace())                