str1="AABBFGTRU"
a=str1.replace(""," ")
b=a.split()
lst1=[]
for i in b:
	if i in  lst1:
		pass
	else:
		lst1.append(i)
c=''.join(lst1)
print(c)