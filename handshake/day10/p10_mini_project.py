#Mini project: login validator using decorator.
"""
Docstring for handshake.day10.p10_mini_project
create an decorator that checks the user information is correct or not 
if it is correct then it will grant the user as successfully registerd/ logined otherwise it will 
shows login unsuccess full
"""

def login_requirnment(func):
    def wrapper(username,password):
        correct_username="admin"
        correct_password="1234"



        if username==correct_username and password==correct_password:
            print("admin login successfully✅")
            return func(username,password)
        
        else:
            print("access failed❌")
    return wrapper
@login_requirnment
def dashboard(username,password):
    print("-------------------------welcome to dashboard----------------------------- ",username)
U=input("enter your valid name: ")
P=input("enter your password: ")
dashboard(U,P)

#this is end of the program