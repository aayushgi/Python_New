#volume of a cuboid
class cuboid:
	def __init__(self,l,b,h):
		self.l=l
		self.b=b
		self.h=h
	def volume(self):
		return(self.l*self.b*self.h)
x=int(input("enter the length of cuboid:"))
y=int(input("enter the breath of cuboid:"))
z=int(input("enter the height of cuboid:"))
v=cuboid(x,y,z)
Volume=v.volume()
print(Volume)