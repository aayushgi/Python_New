class employee:
	def setvalue(self,empid,empname,empsal):
		self.empid=empid
		self.empname=empname
		self.empsal=empsal
	def getvalue(self):
		print("Employee id =",self.empid)
		print("Employee name= ",self.empname)
		print("employee salary= ",self.empsal)
e=employee()
id=int(input("enter your id here: "))
name=input("enter your name here: ")
sal=int(input("enter your salary here: "))
e.setvalue(id,name,sal)
e.getvalue()
"""alwys pass set value in self parameter and use same function used to get value"""