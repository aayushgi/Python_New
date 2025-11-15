# Write a python program to compute gross salary based on following parameters:- 
salary= float(input("enter the basic salary: "))

if salary<=4000:
    hra=0.10*salary
    da=0.50*salary
elif salary<=8000:
    hra=0.15*salary
    da=0.60*salary
elif salary<=12000:
    hra=0.20*salary
    da=0.70*salary
elif salary>12000:
    hra=0.25*salary
    da=0.80*salary
    
gs=salary+hra+da

print("basic salary is: ", salary)
print("HRA is: ", hra)
print("DA is: ", da)
print("gross salary is: ", gs)
