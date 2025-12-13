class parent:
	def __init__(self):
		print("this is parent constructor")
class child(parent):
	def __init__(self):
		super().__init__()
		print("this is child constructor")
obj=child()
##no changes