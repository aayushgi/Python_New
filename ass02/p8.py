#Write a python program to find factorial of given number. 
num=int(input("enter the number which factorail did you want: "))
n=num
if num<0:
	print("factorail is not for the negative numbers")
else:
	fact=1
	while num > 0:
		fact=fact*num
		num=num-1
print("factorail of the", n ,"is",fact)