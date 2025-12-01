class bill:
	def unit(self,u):
		if u>1 and u<=150:
			return(u*2.40)
		elif u>150 and u<=300:
			return((u-150)*3.00+(150*2.40))
		else:
			return((150*2.40)+(150*3.00)+(u-300)*3.20)
b=bill()
u=b.unit(199)
print(u)