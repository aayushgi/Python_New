#filter() to extract odd numbers from list.
number=[2,34,8,997,3,76,99]
odd_number=list(filter(lambda x:x%2 !=0,number))
print(odd_number)