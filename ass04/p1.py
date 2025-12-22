"""Write a python program to create two functions area() and peri() to find area and 
perimeter of rectangle. """
l=int(input("enter the length of the of the rectangle: "))
b=int(input("enter the breath of the rectangle: "))
def area(length,breadth):
	return length*breadth
def peri(length,breadth):
	return 2*(length+breadth)
print("area of rectangle is: ",area(l,b))
print("perimeter of rectangle is:", peri(l,b))

	