# Write a python program to convert binary number to its decimal equivalent
binary=input("enter the binary string here: ")
decimal=0
for digit in binary:
	decimal=decimal*2+int(digit)
print("equivalent decimal is :",decimal)