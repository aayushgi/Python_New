#Write a python program to create a list of ten numbers by taking input from user. 
#Now check a number is presented in list or not. 
def serach(l,n):
	le=len(l)
	for i in range(le):
		if (l[i]==n):
			return 1
	return false
lt=[3, 42, 55, 65, 85, 33]
print(search(lt, 42))