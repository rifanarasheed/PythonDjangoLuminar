from datetime import datetime

class Bank:
    bank_name = "sbi"
    def Create_Account(self,Ano,Aname,Abalance):
        self.Ano = Ano
        self.Aname = Aname
        self.Abalance = Abalance
    def deposit(self,amount):
        self.Abalance+=amount
        print()
    def withdrawal(self,amount):
        if self.Abalance>amount:
            self.Abalance-=amount
            print("your account",self.Ano,"has been debited with amount :",amount,"on",datetime.today(),"Available balance is ",self.Abalance)
        else:
            print("Insufficient balance")
    def bal_enq(self):
        print(self.Abalance)

bank1 = Bank()
bank1.Create_Account(1000,"rif",23000)
bank1.deposit(3000)
bank1.withdrawal(2000)

# static variable
# constuructor
