#dyanamic list
mylist=[]
print("enter the range between 0 to 10")
for i in range(0, 10):
	n=int(input())
	mylist.append(n)
print(mylist)
print("max: ", max(mylist))
print("min: ", min(mylist))