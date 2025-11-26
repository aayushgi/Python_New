str1=input("input a sentense here:")

a=str1.split()
longest=""
for word in a:
	if len(word)>len(longest):
		longest= word
print(longest)