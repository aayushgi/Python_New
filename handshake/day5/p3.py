
#Function to compute factorial of a number.
#type1=by using recursion
n=int(input("enter the number which factorial you want:"))
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print("factorial",factorial(n))
#type2=by using loops
def factorial01(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print("type 2",factorial01(n))
#type 3 by using predefine function
import math
print("factorial type 3",math.factorial(n))
