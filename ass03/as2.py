#Write a python program to create a list of ten numbers by taking input from user. 
#Now check a number is presented in list or not. 
list=[]
print("enter the number in the list: ")
for i in range(0,10):
	n=int(input())
	list.append(n)
print(list)
a=int(input("enter the number you want top check in the list: "))
for i in range(0,10):
	if list[i]==a:
		c=1
if c==1:
	print("the number you are entered is present in the list")
else:
	print("the number you entered not present in the list")