#wap for the elecricity bill calculator
unit=int(input("enter the units you have been used "))
if unit<=150:
	bill=unit*2.40
elif unit>=150 and unit<=300:
	bill=(150*2.40)+(unit-150)*3.0
else:
	bill=(150*2.40)+(150*3.0)+(unit-300)*3.20
print("your bill is : ", bill)