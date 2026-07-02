# Write a python program to create a list of ten numbers by taking input from user. Now find sum and average of numbers.
numbers=[]
print("enter the numbers of the list: ")
for i in range(0,10):
    n=int(input())
    numbers.append(n)
print(numbers)
print("sum of the list is: ",sum(numbers))