#  Write a python program to take coordinates of a point as input and determine its 
x= float(input("enter the vale of x coordinate: "))
y= float(input("enter the value of y coordinate: "))

if x>0 and y>0:
    print("The point lies in the First Quadrant")
elif x<0 and y>0:
    print("The point lies in the Second Quadrant")
elif x<0 and y<0:
    print("The point lies in the Third Quadrant")
elif x>0 and y<~0:
    print("The point lies in the Fourth Quadrant")
else:
    print("The point lies on the Axis")    