try:
 a=int(input("enter the frist num "))
 b=int(input("enter the second num "))
 print("div",a/b)
except ValueError:
	print("invalid input")
except ZeroDivisionError:
	print("not divisible by zero")
finally:
	print("thank you")
