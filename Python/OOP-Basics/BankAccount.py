'''
Bank Account class created by ZXx_Neto_xXZ
A class program for OOP in Python 3
'''
class BankAccount: #creating a new class

    def __init__(self, initial_balance=0): #init for the class objects
        self.final_balance = 0 #the money of the bank account is set to 0
        self.final_balance = initial_balance #the balance of the bank account is set to a value

    def deposit(self, amount): #function to add and update the bank account balance
        self.final_balance += amount

    def withdraw(self, amount): #function to subtract and update the bank account balance
        self.final_balance -= amount

    def interest(self, term, amount): # function to calculate the balance for an amount of money with interest
        intest = (1+(.075/term))**term - 1
        total = intest*amount
        self.deposit(total)

    def getBalance(self):
        return self.final_balance
    

object1 = BankAccount()
print(object1.getBalance())


