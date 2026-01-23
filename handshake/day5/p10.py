#calculator using lambda function
add=lambda a,b: a+b
sub=lambda a,b: a-b
mul=lambda a,b: a*b
div=lambda a,b: a/b
a=int(input("enter frist number here: "))
b=int(input("enter second number here: "))
print("addition",add(a,b))
print("subtraction",sub(a,b))
print("multiplication",mul(a,b))
print("division",div(a,b))