class Student:
	def __init__(self,rollno,name,fee):
		self.rollno=rollno		
		self.name=name
		self.fee=fee
	def getvalue(self):
		print("enter your  roll no",self.rollno)
		print("enter your name",self.name)
		print("enter your fee",self.fee)
r=int(input("enter roll no."))
n=input("enter name")
f=int(input("enter your fee"))
s=Student(r,n,f)
s.getvalue()