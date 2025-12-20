#this program is about multilevel inheritance
class Employee:
    def setEmployee(self, empid, empname):
        self.empid = empid
        self.empname = empname
    def getEmployee(self):
        print("employee id: ", self.empid)
        print("employee name: ", self.empname)
class payroll(Employee):
    def setpayroll(self, bs, hra, da):
        self.bs=bs
        self.hra=hra
        self.da=da
    def getpayroll(self):
        print("basic salary: ", self.bs)
        print("HRA is: ", self.hra)
        print("DA is: ",self.da)
class payslip(payroll):
    def netsalary(self):
        netsal=self.bs + self.hra + self.da
        print("net salary is: ",netsal)
eid=int(input("enter employee id here: "))
ename=input("enter employee name here: ")
b=float(input("enter your basic salary here: "))
h=float(input("enter your HRA here: "))
d=float(input("enter your DA here: "))
ps=payslip()
ps.setEmployee(eid, ename)
ps.setpayroll(b,h,d)
class payslip(payroll):
    def netSalary(self):
        print("net salary is :",self.bs+self.hra+self.da)
eid=int(input("enter employee id here: "))
ename=input("enter employee name here: ")
b=float(input("enter your basic salary here: "))
h=float(input("enter your House rent allowance  here: "))
d=float(input("enter your Dearness allowance here: "))
ps=payslip()
ps.setEmployee(eid, ename)
ps.setpayroll(b,h,d)
print("\n---Employee Details---")
ps.getEmployee()
print("\n---Payroll Details---")
ps.getpayroll()
print("\n---Net Salary---")
ps.netSalary()
