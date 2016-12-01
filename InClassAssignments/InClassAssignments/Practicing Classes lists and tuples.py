#parents, babies = (1, 80)
#while babies < 100:
    #print ("This generation has {0} babies".format(babies))
    #parents, babies = (babies, parents + babies)

class BankAccount(object):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def overdrawn(self):
        return self.balance < 0
my_account = BankAccount(15)
my_account.withdraw(5)
my_account.deposit(int(input("How Much? ")))
print (my_account.balance)