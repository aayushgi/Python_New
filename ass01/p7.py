#WAP to covert days into years
days=int(input("enter the numbers of days : "))

y= days//365
s= days%365

r= s//7
d= s%7


print(" years " , y , " weaks " , r , "day" , d)
