user=input("enter the  string to check for palendrom")
rev=""
for i in user:
	rev=i+rev
print(rev)
if rev==user:
	print("yes")
else:
	print("no")