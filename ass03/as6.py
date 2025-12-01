"""Write a python program to find number of occurrences of each vowel present in the 
given string? """
text=input("enter the sentense here: ")
text=text.lower()
print(text)
vowel="aeiou"
print("occurence of vowel in the given string: ")
for v in vowel:
	count=text.count(v)
	print(v,"=",count)