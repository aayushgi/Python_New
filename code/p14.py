#ladder if else
num1=int(input("enter frist number: "))
num2=int(input("enter second number: "))
num3=int(input("enter third number: "))
if num1>num2 and num1>num3:
    print(num1,"is gratest")
elif num2>num1 and num2>num3:
    print(num2,"is gratest")
else:
    print(num3,"is gratest")