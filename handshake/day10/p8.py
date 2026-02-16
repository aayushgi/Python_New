#Compare list vs generator memory (sys.getsizeof).
import sys

# List 
my_list = [i for i in range(100000)]

# Generator 
my_gen = (i for i in range(100000))

print("List memory:", sys.getsizeof(my_list))
print("Generator memory:", sys.getsizeof(my_gen))
