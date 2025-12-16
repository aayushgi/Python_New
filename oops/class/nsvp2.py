class employee:
    def setValue(self, empid,empname,emapsal):
        self.empid=empid
        self.empname=empname
        self.empsal=emapsal
    def display(self):
        print("Employee ID: ", self.empid)
        print("Employee name: ", self.empname)
        print("Employee salary: ", self.empsal)
e=employee()#object creation
eid=int(input("enter your id here: "))
emane=input("enter your name here: ")
esal=float(input("enter your salary here: "))
e.setValue(eid, emane, esal)
e.display()#function calling    