class rectangle:
    def __init__(self):
        self.l=l
        self.b=b
    def rectarea(self):
        return self.l*self.b
    def rectperi(self):
        return 2*(self.l+self.b)
x=int(input("enter the length of rectangle: "))
y=int(input("enter the breath of rectangle: "))
r=rectangle(x,y)
print("area of retangle is: ", r.rectarea())
print("primeter of rectangle is: ", r.rectperi())