#Use logical operators to check multiple conditions.
#using and operator
age= int(input("Enter your age: "))
marks=int(input("Enter your marks: "))
if age>=18 and marks>=80:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")
#using or operator
username = "ayush"
email_verified = False
phone_verified = True

if email_verified or phone_verified:
    print("User verification successful")
else:
    print("User verification failed")
#using not operator
is_raining = False
if not is_raining:
    print("It's a sunny day, go outside!")  
 

