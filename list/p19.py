#wap to get 5number from user and then find the sum
numlist=[]
print("enter the 5 numbers for get the sum")
for i in range(0, 5):
	num=int(input())
	numlist.append(num)
	
print(num)
for i in range(0, 5):
	sum = sum + numlist[i]

print(sum)