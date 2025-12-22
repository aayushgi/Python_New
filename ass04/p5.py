"""Write a python program to create a function named rev(), in rev() function pass a 
string and this function return reverse string. """
def rev(string):
    reverse=""
    for char in string:
        reverse=char+reverse
    return reverse
string=input("enter the string here: ")
print("revese of thr string is: ",rev(string))    