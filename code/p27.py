def rev(s):
    r=" "
    for ch in s:
        r=ch+r
    return r
text=input("enter the string: ")
print("reversed string is",rev(text))