#Print pattern using nested loop: *, **, ***.
for i in range(1,4):
    print("*"*i)

#and 
for i in range(1,4):
    for j in range(i):
        print("*", end="")    
    print()