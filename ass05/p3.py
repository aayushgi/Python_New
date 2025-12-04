""" Write a python program to create a class with name ‘Rectangle’. In ‘Rectangle’ class 
take two instance variables length and breadth. Now create a parameterized 
constructor to initialize variables and create a method area() which return area of 
rectangle. Test the class ‘Rectangle’. """
class Rectangle:
	def __init__(self,l,b):
		self.l=l
		self.b=b
	def area(self):
		return self.l*self.b
x=int(input("enter the length of the rectangle: "))
y=int(input("enter the breath of the rectangle: "))
r=Rectangle(x,y)
print("area of the rectangle is: ",r.area())