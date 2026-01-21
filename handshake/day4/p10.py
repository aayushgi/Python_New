num=int(input("enter the number which you want to count: "))
count=0
while num!=0:
    num=num//10
    count +=1
print("total count: ",count)