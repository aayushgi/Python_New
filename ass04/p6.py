"""Write a python program to find factorial of given number using ‘Recursion’."""
def factorial(n):
    if n==0 or n==1:
        return 1
    else: 
        return n*factorial(n-1)
num=int(input("enter the number to find the factorial: "))
print("factorial of ",num, "is", factorial(num))