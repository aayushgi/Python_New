#multiple inheritance

class A:
	def m1(self):
		print("m1 function from class A	")
class B():
	def m2(self):
		print("m2 function from class B")
class C(A,B):
	def m3(self):
		print("m3 function from class C")
c=C()
c.m3()
c.m2()
c.m1()