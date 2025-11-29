# Write a python program to print Fibonacci series up to n terms, where value of n is 
#entered by user 
n=int(input("enter the number of term did you want: "))
a,b=0,1
i=0
print("fibonacci series")
while i<n:
	if i<=1:
		print(i, end=" ")
	else:
		nxt=a+b
		print(nxt, end=" ")
		a,b=b,nxt
	i=i+1
print()
		

	