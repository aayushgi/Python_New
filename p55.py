#simple calculator
class SimCal:
	def add(self,x,y):
		return(x+y)
	def sub(self,x,y):
		return(x-y)
	def mul(self,x,y):
		return(x*y)
	def div(self,x,y):
		return(x/y)
sc=SimCal()
sum=sc.add(10,20)
print(sum)
min=sc.sub(10,20)
print(min)
multiply=sc.mul(10,20)
print(multiply)
division=sc.div(10,20)
print(division)