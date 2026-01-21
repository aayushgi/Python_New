#Demonstrate break in loop execution.
for i in range(1 , 100):
    if i == 99:
        break
    print(i)