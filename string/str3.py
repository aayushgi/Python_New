user=input("enter the random string")
v=0
c=0
vowel="aeiou"
for i in user:
	if i.lower() in vowel:
		v=v+1
	else:
		c=c+1
print("number of vowels", v)
print("number of consonent", c)