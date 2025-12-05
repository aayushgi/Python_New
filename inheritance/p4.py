class Base:
	def showBase(self):
		print("This meaasge from from base class")
class Derived(Base):
	def showDerived(self):
		print("this message from derived class")
b=Derived()
b.showDerived()
b.showBase()