#15. Write a python program to check given number is Armstrong or not. 
num=int(input("enter the number here to check is it armstrong or not"))
temp=num
result=0
c=len(str(num))
while num>0:
	rem=num%10
	result=result+(rem**c)
	num=num//10
if result==temp:
	print(temp,"number is armstrong")
else:
	print(temp,"number is not a armstrong")