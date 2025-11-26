#Write a python program to calculate electricity bill based on following parameters:- 
unit=int(input("enter the units that you have been used: "))
if unit>1 and unit<=150:
	bill=unit*2.40
elif unit>150 and unit<=300:
	bill=(150*2.40)+(unit-150)*3
elif unit>300:
	bill=(150*2.40)+(150*3)+(unit-300)*3.20
print("total unit used",unit,
"your bill",bill)