#wap to check the avilability
list=[]
print("enter the 10 numbers in the list: ")
for i in range(0, 10):
	n=int(input())
	list.append(n)
print(list)
a=int(input("enter the number you want to check: "))
for i in range(0, 10):
	if list[i]==a:
		c=1
if c==1:
	print("not present in the list")	
else:
	print("found")
	