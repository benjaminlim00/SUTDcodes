class Account:
    def __init__(self, owner, account_number, amount):
        self._owner = owner
        self._account_number = account_number
        self._balance = amount
        
    def deposit(self, amount):
        self._balance += amount
    def withdraw(self, amount):
        self._balance -= amount
    def __str__(self):
        return "{}, {}, balance: {}".format(self._owner, self._account_number, self._balance)
    
a2 = Account ('Liz Olsson' , '19371564761' , 20000)
a1 . deposit (1000)
a1 . withdraw (4000)
a2 . withdraw (10500)
a1 . withdraw (3500)
print(a1)
