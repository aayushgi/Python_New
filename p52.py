num=int(input("enter the number "))
temp=num
c=len(str(num))
result=0
while num>=0:
	rem=num%10
	resut+=rem**c
	num=num//10
if result==temp:
	print(temp,"armstrong number")
else:
	print(temp,"not armstrong")
	