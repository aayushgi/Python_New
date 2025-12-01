name=input("enter your full name ")
st=name.split()
short=""
for i in range(len(st)-1):
	short=short+st[i][0].upper()+"."
short=short+st[-1].title()
print(short)
