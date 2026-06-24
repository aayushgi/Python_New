#Write a python program to find simple interest. si=(p*n*r)/100
p = float(input("Enter principal amount: "))
n = float(input("Enter time (in years): "))
r = float(input("Enter rate of interest: "))
si = (p * n * r) / 100
print("Simple Interest =", si)