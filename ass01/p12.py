#WAP to check the weather according to weather entered
temp= int(input("enter the current temperature"))
if temp<0:
	print("freezing weather")
elif temp>0 and temp<10:
        print("very cold weather")
elif temp>=11 and temp<20:
        print("cold weather")
elif temp>=21 and temp<30:
	print("normal")
elif temp>=31 and temp<40:
	print("hot")
elif temp>=40:
	print("very hot")
else:
	peint("invalid input")