
#Decorator converting output to uppercase.
def to_uppercase(func):
    def wrapper():
        result=func()
        return result.upper()
    return wrapper




@to_uppercase
def greet():
    return "hellow"


print(greet())