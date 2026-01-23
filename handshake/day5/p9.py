#reduce() to find sum of list.
from functools import reduce
number=[5,6,7,8,9,10]
result=reduce(lambda x,y:y+x,number)
print(result)