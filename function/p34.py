#WAP of recursion (factorial )in functions 
def fact(n):
	if n==0 or n==1:
		return 1
	else:
		return n*fact(n-1)
x=int(input("enter the number which factorial did you want"))
f=fact(x)
print("the factorial of", x , "is", f)
