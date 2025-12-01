#Write a python program to create a list of ten numbers by taking input from user 
#named AR. Now copy even numbers in list EAR and odd numbers in list OAR. Now 
#display elements of EAR and OAR.
AR=[]
EAR=[]
OAR=[]
for i in range(10):
	num=int(input("enter the number: "))
	AR.append(num)
print(AR)
for n in AR:
	if n % 2==0:
		EAR.append(n)
	else:
		OAR.append(n)
print("list of even numbers: ",EAR)
print("list of odd numbers: ",OAR)