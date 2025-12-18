#file handling program
f=open("emp.doc","a")
empid=int(input("enter your id here: "))
empname=input("enter your name here: ")
f.write("employee id: "+str(empid)+"\nemployee name: "+str(empname))
f.close()
print("information save")