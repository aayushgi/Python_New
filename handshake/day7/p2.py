#Reverse a string without built-in functions.
text=input("enter the string here: ")
rev=""
for ch in text:
    rev=ch+rev
print(rev)