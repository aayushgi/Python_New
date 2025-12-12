from abc import ABC, abstractmethod
class shape(ABC):
	def area(self):
		pass
	def perimeter(self):
		pass
class rectangle(shape):
	def area(self):
		print("area=",length*breath)
	def perimeter(self):
		print("perimeter=" ,2*(length+breath))
length=int(input("length of the rectangle"))
breath=int(input("breath of the rectangle"))
obj=rectangle()
obj.area()
obj.perimeter()
