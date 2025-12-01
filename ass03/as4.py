"""Write a python program to create a list of five students by taking input from user. 
Now display name of students in ascending and descending order. """
list=[]
print("enter the students name here: ")
for i in range(5):
	name=input("enter name here: ")
	list.append(name)
print(list)
list.sort()
print("list in ascending order: ",list)
list.sort(reverse=True)
print("list in descending order: ",list)