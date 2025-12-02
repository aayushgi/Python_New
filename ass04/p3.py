"""
Write a python program to create a function search(), in search function pass two 
parameters first, a list of ten numbers and second, a number to search. If number is 
present in list return index of list otherwise return false. 
"""
def search(list1,n):
	for i in range(len(list1)):
		if list1[i]==n:
			return i
	return False
numbers=[]
print("enter the numbers here: ")
for i in range(10):
	numbers.append(int(input()))
input=int(input("enter the value you want to search: "))
answer=search(numbers,value)
if answer == False:
	print("not present in the list")
else:
	print("not present in the list")