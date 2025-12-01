class Rectangle:
	def __init__(self,l,b):
		self.l=l
		self.b=b 
	def rarea(self):
		return(self.l*self.b)
	def rperi(self):	
		return(2*(self.l+self.b))
x=int(input("enter length"))
y=int(input("enter breath"))
r=Rectangle(x,y)
area=r.rarea()
peri=r.rperi()
print("area of rectangle:",area)
print("perimeter  of rectangle: ",peri)