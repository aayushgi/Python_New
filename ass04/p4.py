"""Write a python program to create a function named substr(), in substr() function 
pass a string and substring. If substring is presented in string then return true or 
return false.
"""
def substr(string, substring):
    if substring in string:
        return True
    else: 
        return False
string=input("enter the string here: ")
substring=input("enter the substring here: ")
print(substr(string, substring))
