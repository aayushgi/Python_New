##this program is about multiple inheritance
class A:
    def m1(self):
        print("this is function m1 from class A")
class B:
    def m2(self):
        print("this is function m2 from class B")
class C(A,B):#multiple classes are inherited
    def m3(self):
        print("this is function m3 from class c")
c=C()
c.m1()
c.m2()
c.m3()
#creating object for class c only we can call every function of that inherited class