#Write a python program to take number of days as input now display years, weeks and days. E.g. If user input 375 days then output will be 1 years, 1 weeks and 3 days. In this program ignore leap year. 
days=int(input("enter the number of days here: "))
year=days//365
remaining=days%365
weaks=remaining//7
day=remaining%7
print("years: ",year)
print("weaks ",weaks)
print("days: ",day)