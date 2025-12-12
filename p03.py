class parent:
	def add(self,x,y):
		return x-y
class child(parent):
	def add(self,x,y):
		s=super().add(x,y)#this function used to correct the parent class
		print("this is returned from parent class having wrong result",s)
		return x+y
c=child()
res1=c.add(10,20)
print("this is child class to correcting the fault of parent class",res1)
