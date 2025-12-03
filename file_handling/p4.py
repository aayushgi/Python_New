#develop a program in python to perform read operation from file 
f=None#code will run without this line
try:
	filename=input("enter filename to be opened: ")
	f=open(filename,"r")
	contents=f.read()
	print(contents)
except FileNonFoundError:
	print("file not found")