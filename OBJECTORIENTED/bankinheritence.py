# private method

class Bank:
    def withdraw(self):
        print("inside withdraw")
    def bal_enq(self):
        print("inside enquire")
    def __deposit(self):                       # private method (__method name) --> it can accessed only inside class by self keyword
        print("inside deposit")
    def mcall(self):
        self.__deposit()                       # accessing private method inside the class

class Atm(Bank):
    pass

bank = Bank()
atm = Atm()
atm.withdraw()
atm.bal_enq()
atm._Bank__deposit()               # if want to Access private method of Bank class(obj._classname__privatemethod)
bank._Bank__deposit()

