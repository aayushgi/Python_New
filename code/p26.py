#WAP in python to find volume of cuboid using user defined function
def volume(l,b,h):
    return (l*b*h)
x=int(input("enter the length ofbthe cuboid: "))
y=int(input("enter the breath of the cuboid: "))
z=int(input("enter the height of the cuboid: "))
v=volume(x,y,z)
print("volume of the cuboid is: ",v)