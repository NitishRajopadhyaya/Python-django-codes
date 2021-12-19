import itertools 

accounts ={}

class Account:

     count = itertools.count(start=1)  
     def __init__(self,name,balance,pin):
         accnum = next(self.count) 
         self.accnum = accnum
         self.pin= pin
         self.name = name
         self.balance = balance
         accounts[accnum] = self
         print("Hi",self.name,"Your Account has been created with Rs",self.balance)
         
     def  change_pin(self,old_pin,new_pin):
         if old_pin==self.pin:
             self.pin=new_pin
         else:
              print("Your old pin is invalid")
     def transfer(self,pin,reciever_name,reciever_accnum,amount):
          if pin==self.pin:
               if self.balance>=amount:
                     if accounts.get(reciever_accnum)!=None: 
                        reciever = accounts.get(reciever_accnum)
                        if  self.name==reciever_name: 
                                print("you cannot Transfer into your own account")

                                
                        else:
                                new_sender_balance = self.balance - amount 
                                self.balance = new_sender_balance 

                                new_reciever_balance = reciever.balance + amount
                                reciever.balance = new_reciever_balance
                                print("Your new balance is",self.balance)
                     else:
                         print("sorry the reciever doesn't exists")
               else:
                  print("Your balance is insufficent")
          else:
              print("Your pin is incorrect. please try again.")

     
my = Account(name="Nitish",balance=50000,pin=123)
your = Account(name="Hari",balance=1200,pin=234)

print(my.accnum,your.accnum)
print(accounts)

my.transfer(pin=123,reciever_name="Hari", reciever_accnum=2,amount= 200)
your.transfer(pin=234, reciever_name="Hari",reciever_accnum=2,amount=200)

