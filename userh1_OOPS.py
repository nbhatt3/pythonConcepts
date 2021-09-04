# Bank User has name and account. There are two types of Users
# Normal and privileged user . There are two types of privileged
# users, Gold and Silver. Gold has cashback of 5% and Silver has 
# cashback of 3% of expenditure when they spend any cash 

class NotEnoughBalance(Exception):
    pass


class BankAccount:
    def __init__(self, initAmount):  # 1
        self.amount = initAmount
        print("In Init BankAccount", str(self.amount))

    def transact(self, amount):  # 2
        if self.amount + amount < 0:
            print("In BankAccount transact method with amount less than zero: ", amount)
            raise NotEnoughBalance("not possible")
            print("Amount is ", self.amount + amount)
        
        print("Amount sent in BankAccount transact method is ", amount)
        self.amount += amount
        print("Updated Amount in BankAccount is ", str(self.amount))

    def __str__(self):  # 3
        return "BankAccount(" + str(self.amount) + ")"


# Has relation - containment
# is relation - inheritance

from abc import ABCMeta, abstractmethod

class BankUser(metaclass=ABCMeta):  # template
    # class variable
    how_many_users = {'TotalUsers': 0}  # BankUser.how_many_users
    print("START")
    def __init__(self, name, initAmount):
        self.name = name  # instance variable
        self.account = BankAccount(initAmount)
        #print("In init BankUser")
        self.update_user_types()
        
    def update_user_types(self):
        t = self.getUserType()
        if t in BankUser.how_many_users:
            BankUser.how_many_users[t] += 1
        else:
            BankUser.how_many_users[t] = 1
        BankUser.how_many_users['TotalUsers'] += 1

    def __str__(self):
        #print("In BankUser , getUserType()")
        return "%s(%s,%s)" % (self.getUserType(), self.name, self.account)
        
    # class Method are accessed by class_name.method
    @classmethod
    def how_many(cls):
        return cls.how_many_users

    # applying a decorator
    @abstractmethod
    def getCashbackPercentage(self):
        return 0

    @abstractmethod
    def getUserType(self):
        pass

    def transact(self, amount):
        try:
            self.account.transact(amount)
            print("In BankUser transact method with Amount", amount)
            if amount < 0:
                print("In transact method")
                cashback = self.getCashbackPercentage() * abs(amount)
                self.account.transact(cashback)
                print("Amount is less than 0, Cashback is " , str(cashback))
        except NotEnoughBalance as ex:
            print(str(ex), "Name:", self.name, "Amount:", amount)


class NormalUser(BankUser):
    def getCashbackPercentage(self):
        return super().getCashbackPercentage()

    def getUserType(self):
        return "NormalUser"


class SilverUser(BankUser):
    def getCashbackPercentage(self):
        return 0.03

    def getUserType(self):
        return "SilverUser"

class GoldUser(BankUser):
    def getCashbackPercentage(self):
        return 0.05

    def getUserType(self):
       # print("In getUserType Gold")
        return "GoldUser"


# script __name__ would be __main
# in module __name__ would be filename
if __name__ == '__main__':  # pragma: no cover
    # bu = BankUser("Bank", 100)
    users = [GoldUser("Gold", 100)]
    #users = [GoldUser("Gold", 100), SilverUser("Silver", 100),
     #        NormalUser("Normal", 100)]
    amounts = [100, -200, 300, -400, 400]
    for u in users:
        print(u)
        for am in amounts:
            # print(u, 'Amount:', am)
            u.transact(am)
        # print(u)
print(BankUser.how_many())
