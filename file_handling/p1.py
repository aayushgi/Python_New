#develop a program in python to perform write operation into a file 
f=open("emp.txt","w") 
empid=int(input("enter the id: "))
empname=input("enter name here: ")
salary=int(input("enter your salary here: "))
f.write("employee id"+str(empid)+"\n"+"employee name: "+str(empname)+"\n"+"employee salary: "+str(salary)+"\n")
f.close()
print("information saved")