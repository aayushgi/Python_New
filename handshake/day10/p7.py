
#Create nested decorators adding HTML tags.
def bold(func):
    def wrap():
        return "<b>" + func() + "</b>"
    return wrap


def italic(func):
    def wrap():
        return "<i>" + func() + "</i>"
    return wrap


@bold
@italic
def greet():
    return "Hello"

print(greet())
