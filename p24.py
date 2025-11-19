#function to count vowels in a strings
def cv(s):
	vowels="aeiouAEIOU"
	count=0
	for ch in s:
		if ch in vowels:
			count=count+1
	return count
print(cv("education"))	