#function to count even or odd in a list
def ceo(list):
	even=0
	odd=0
	for i in list:
		if i%2==0:
			even=even+1
		else:
			odd=odd+1
	print("number of even :", even)
	print("number of odd :", odd)
print(ceo([10, 20, 30, 40]))

	
	
	