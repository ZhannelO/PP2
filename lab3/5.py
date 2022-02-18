class Account():
    def __init__(self,owner,balance): 
        self.owner=owner
        self.balance=balance
    def withdraw(self,amount):
        if self.balance-amount<= 0:
            pass
        else:
            current=str(self.balance-amount)
            return str(self.owner)+"'s current ballance:"+current +" "+" "+"Expenses:"+"-"+str(amount)
    def deposit(self,savings):
        self.balance+=savings
        new=str(self.balance)
        return str(self.owner)+"'s new balance:"+new+ " "+" "+"Income:"+"+"+str(savings)
owner=Account("Zhannel",5000)
print(owner.withdraw(1000))
print(owner.withdraw(2000))
print(owner.withdraw(10000))
print(owner.deposit(10000))
person=Account("Camilla",7000)
print(person.withdraw(3000))


