"""Write a python program to create a class with name ‘Employee’. In Employee class 
take three instance variables empid, empname and salary. Create two methods in 
Employee class first setEmployee() and second display(). setEmployee() method 
initialize instance variables empid, empname, salary and display() method display 
value of empid, empname and salary. Now test Employee class. """
class Employee:
	def setValue(self,empid,empname,salary):
		self.empid=empid
		self.empname=empname
		self.salary=salary
	def display(self):
		print("Employee id= ",self.empid)
		print("Employee name= ",self.empname)
		print("Employee salary= ",self.salary)
e=Employee()
eid=int(input("enter your employee id here: "))
ename=input("enter your name here: ")
esal=int(input("enter your salary here: "))
e.setValue(eid,ename,esal)
e.display()