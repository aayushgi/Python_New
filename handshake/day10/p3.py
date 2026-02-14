
#Create decorator counting function calls.
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"{func.__name__} has been called {wrapper.calls} times")
        return func(*args, **kwargs)
    
    wrapper.calls = 0
    return wrapper


@count_calls
def greet(name):
    print(f"Hello {name}")


greet("Ayush")
greet("Rahul")
