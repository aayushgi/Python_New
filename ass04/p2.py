import mycal
def calc(a,b):
	sum=a+b
	sub=a-b
	mul=a*b
	div=a/b
	return(["sum is",sum, "substarction is", sub, "multiplication is", mul, "division is",div])

a=int(input("enter the frist number"))
b=int(input("enter the second number"))
c=calc(a,b)
print(c)
