from datetime import datetime

class Bank:
    bank_name = "sbi"                                                                 # bank_name is a static variable as it is same for every customer in this scenario
    def __init__(self,Ano,Aname,Abalance):
        self.Ano = Ano                                                                # instance variable intialization
        self.Aname = Aname
        self.Abalance = Abalance
    def deposit(self,amount):
        self.Abalance+=amount
        print("your bank name :",Bank.bank_name)                                      # static variable can be accesed by class name.staticvariable
        print("your account",self.Ano,"has been credited with amount :",amount,"on",datetime.today(),"Available balance is ",self.Abalance)
    def withdrawal(self,amount):
        if self.Abalance>amount:
            self.Abalance-=amount
            print("your bank name :", Bank.bank_name)
            print("your account",self.Ano,"has been debited with amount :",amount,"on",datetime.today(),"Available balance is ",self.Abalance)
        else:
            print("Insufficient balance")
    def bal_enq(self):
        print("Balance : ",self.Abalance)

bank1= Bank(1000,"rif",23000)
bank1.deposit(3000)
bank1.withdrawal(2000)


# there are two kinds of variable in class :
# static variable and instance variable
