
#Create calculator.py with add, sub, mul functions
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
x=int(input("enter frist number here: "))
y=int(input("enter second number here: "))
print("addition",add(x,y))
print("substraction",sub(x,y))
print("multiplicaton",mul(x,y))