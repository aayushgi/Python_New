#function to check even or odd
x=int(input("enter an number"))
def check(x):
	if x%2==0:
		return 'even'
	else:
		return 'odd'
print(check(x))
	