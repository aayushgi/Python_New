#Create package geometry with circle.py and rectangle.py modules.
def circle_area(r):
    return 3.14* r*r
def circle_circumference(r):
    return 2* 3.14*r
def rectangle_area(l,w):
    return l*w
def rectangle_perimeter(l,w):
    return 2*(l+w)


print("area of circle is ",circle_area(5))
print("circumference of circle",circle_circumference(5))
print("area f rectnagle is",rectangle_area(5,10))
print("perimeter of rectangle is",rectangle_perimeter(5,10))