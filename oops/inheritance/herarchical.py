#this program is about hererachical inheritance
class shape:
    def setValue(self,s):
        self.s=s
class squre(shape):
    def area(self):
        return self.s*self.s
class cube(shape):
    def volume(self):
        return self.s*self.s*self.s
x=int(input("enter the value of squre: "))
sq=squre()
sq.setValue(x)
print("area of squre: ",sq.area())
x=int(input("enter the value of cube: "))
cu=cube()
cu.setValue(x)
print("volume of the cube is: ",cu.volume())