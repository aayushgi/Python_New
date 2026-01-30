#Write Python program to count vowels in a string.
str=input("enter an string here: ")
vowel="aeiouAEIOU"
count=0
for ch in str:
    if ch in vowel:
        count +=1
print(count)