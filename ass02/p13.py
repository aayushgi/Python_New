# Write a python program to print series of prime numbers in given range. Range 
#must be created by taking input from user

s=int(input("enter the starting :"))
e=int(input("enter the ending :"))
for i in range(s, e+1, 1):
	f=0
	for j in range(1, i+1):
		if(i%j==0):
			f=f+1
	if(f==2):
		print(f"{i} is prime ") 