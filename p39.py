# WAP to convert temperature 
print("enter 1 for C to F")
print("enter 2 for F to C")

ch = int(input("Enter your choice: "))

if ch == 1:
    c = float(input("Enter the temperature in Celsius: "))
    f = (9 * c) / 5 + 32
    print("Temperature in Fahrenheit:", f)

elif ch == 2:
    f = float(input("Enter the temperature in Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print("Temperature in Celsius:", c)

else:
    print("Invalid choice")
