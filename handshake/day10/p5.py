
#Decorator logging function execution time.
import time

def log_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Time taken:", end - start)
    return wrapper


@log_time
def test():
    time.sleep(2)
    print("Hello")

test()
