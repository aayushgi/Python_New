#Count frequency of characters using dictionary.
str=input("enter the string: ")
freq={}
for ch in str:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)