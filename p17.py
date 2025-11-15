#dynamic naming
mylist=[]
print("enter you 5 friends name ")
for i in range(0,5):
	n=input()
	mylist.append(n)
print("before sorting: ", mylist)
mylist.sort()
print("after sorting: ", mylist)