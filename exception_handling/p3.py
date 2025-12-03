def  div(x,y):
	try:
		result=x/y
	except ZeroDivisionError:
		
		print("not divisible by zero")
	
	else:
		print("result= ",result)
	finally:
		print("this is finally block")
a=int(input("enter the frist number here "))
b=int(input("enter the second number here "))
div(a,b)