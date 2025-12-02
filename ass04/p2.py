"""
Write a python program to create a function calc(), write code to find summation, 
subtraction, multiplication and division and return result in form of list. Now test 
calc() function. 

"""
def calculator(a,b,op):
	if op=='+':
		return a+b
	elif op=='-':
		return a-b
	elif op=='*':
		return a*b
	elif op=='/':
		if b!=0:
			return a/b
		else:
			return "division not possibile with 0"
	else:
		return "invalid input"
n1=int(input("enter the frist value here: "))
n2=int(input("enter the second value here: "))
print("choose an operator have to be perform: + - * /")
operator=input("enter the operator here:  ")
result=calculator(n1,n2,operator)
print("result= ",result)