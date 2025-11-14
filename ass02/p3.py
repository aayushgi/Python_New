#WAP to find the roots of the quadratic equation
import math

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

# Calculate discriminant
d = b*b - 4*a*c

if d > 0:
    # Two distinct real roots
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("Two Real and Distinct Roots:")
    print("Root 1 =", root1)
    print("Root 2 =", root2)

elif d == 0:
    # One real equal root
    root = -b / (2 * a)
    print("Two Real and Equal Roots:")
    print("Root =", root)

else:
    # Complex roots
    real = -b / (2 * a)
    imag = math.sqrt(-d) / (2 * a)
    print("Complex Roots:")
    print("Root 1 =", real, "+", imag, "i")
    print("Root 2 =", real, "-", imag, "i")