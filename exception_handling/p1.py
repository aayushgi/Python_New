#simple calculator
try:
	a=int(input("enter the frist number here"))
	b=int(input("ennter the second"))
	print("sum: ",a+b)
except ValueError:
	print("wrong input")