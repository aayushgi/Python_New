#Write a python program to find sum of digits of given number. 
num=int(input("enter the number here: "))
if num<0:
	print("enter only positive values")
else:
	sum_digit=0
	n=num
	while n>0:
		digit=n%10
		sum_digit=sum_digit+digit
		n=n//10
print("sum of the",num,"is",sum_digit)