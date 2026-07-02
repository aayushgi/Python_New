#Write a python program to create a list of ten numbers by taking input from user. Now check a number is presented in list or not. 
num=[]
print("enter the numbers of the list: ")
for i in range(0,10):
    n=int(input())
    num.append(n)
print(num)
search=int(input("enter the nuber want to search: "))
if search==num:
    print("number is present in the list: ")
else:
    print("number is not present in the list: ")