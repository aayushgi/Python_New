#Write and read content from a text file.

file = open("data.txt", "w")
file.write("Hello, file handling")
file.close()
#program to save the employee information
f=open("emp.doc","a") 
empid=int(input("enter the id: "))
empname=input("enter name here: ")
salary=int(input("enter your salary here: "))
f.write("employee id"+str(empid)+"\n"+"employee name: "+str(empname)+"\n"+"employee salary: "+str(salary)+"\n")
f.close()
print("information saved")