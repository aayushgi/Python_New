# Write a python program to reverse the digits of given number. 
num=int(input("enter the the number you want to reverse "))
temp=0
n=num
while n>0:
	
	rem=n%10
	temp=temp*10+rem
	n=n//10
print("the reverse of the",num,"is",temp)
#no changes