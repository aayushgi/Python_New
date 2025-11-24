#WAP to print fibonacci series upto n terms 
n=int(input("enter the range you want"))
n1=0
n2=1
print("fibonacci series :")
print(n1, n2, end=" ")
i=1
while(i<=n-2):
	n3=n1+n2
	print(n3, end=" ")
	n1=n2
	n2=n3
	i=i+1