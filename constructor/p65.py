class Bank:
	def __init__(self,acno,name,balance):
		self.acno=acno
		self.name=name
		self.balance=balance
	def deposit(self,dipo):
		self.dipo=dipo
		return(self.balance+self.dipo)
	def withdraw(self,w):
 		if self.balance>=w:
			self.withdraw = w
			return(self.balance-self.withdraw)
		else:
			return "wrong"
	

	
a=int(input("account number"))
n=input("name")
b=int(input("balance"))
B=Bank(a,n,b)

n=int(input("Press no for required opration : "))
if n==1:
  d=eval(input("Enter Diposit Amount : "))
  x=b.deposite(d)
  print("Total Amount after Deposit in Bank : ",x)
elif n==2:
  w=eval(input("Enter  WithDraw amount : "))
  y=b.withdraw(w)
  print("Total Balance after withdraw : ",y)
elif n==3:
    q=b.enquiry(acno,name,balance)
    print(q)
else:
  print("Plzz press any 1/2/3 number for required opration.")

