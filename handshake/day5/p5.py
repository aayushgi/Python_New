#Demonstrate positional, keyword, and default arguments.
#positional 
def student(name, age=18, city="Delhi"):
    print(name, age, city)

student("Rahul")
student("Ayush", 20)
student(name="Aman", city="Mumbai")
