class Shape:
	def setValue(self,a):
		return(a)	
class Squre(Shape):
	def area(self,a):
		return(a*a)
class Cube(Squre):
	def volume(self,a):
		return(a*a*a) 
x=int(input("enter the length of the shape"))
c=Cube()

d=c.volume(x)
a=c.area(x)
print("volume of the shape is: ",d)
print("area of the shape is: ",a)