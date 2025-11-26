#Write a python program to create a list of ten numbers by taking input from user. 
#Now find sum and average of numbers. 
list=[]
print("enter the ten number in the list")
for i in range(0,10):
	n=int(input())
	list.append(n)
print(list)
sum=0#we have to frist declear the sum = 0
for i in range(0,10):
	sum=sum+list[i]
print("sum of the elements of the list", sum)