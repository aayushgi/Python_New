class A:
    def showA(self):
        print("this is function from class a/this is perent class")
class B(A):#class A inherited
    def showB(self):
        print("this is function from class b/this is child class")

b=B()#creation of object of class B
b.showA()#class A calling
b.showB()#class B is calling 