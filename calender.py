from calendar import *
year=int(input("Enter year : "))
x=isleap(year)
print(x)
if x==True:
    print(year," is leap year.")
else:
    print(year, " is not a leap year.")