class BankAccount:
    def __init__(self, initAmount):     #method 1
        self.amount = initAmount

    def transact(self, amount):     #method 2
        self.amount += amount

    def __str__(self):
        return "BankAccount(" + str(self.amount) + ")"

#script used for quick testing
if __name__ == '__main__':
    ba = BankAccount(100)       #calls method 1 - to initialize the class BankAccount.__init__(ba,100), internally with 2 args
    ba.transact(250)            #calls method 2, calls BankAccount,transact(ba.250), internally with 2 args
    print(ba)                   #calls __str__(ba)

#Note: self is not a keyword, it is just a placeholder, we can use other variable name in place of self here.

#Note: __str__ ,etc are special methods in python