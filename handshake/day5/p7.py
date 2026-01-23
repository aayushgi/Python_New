#map() to convert Celsius to Fahrenheit list.
celsius=[20,30.89,112,67]
fahrenheit=list(map(lambda c:(c*9/5)+32,celsius))
print("temperature in fahrenheit",fahrenheit)