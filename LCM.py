a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))

mxno=max(a,b)
while (True):
    if (mxno%a==0) and (mxno%b==0):
        break
    mxno=mxno+1
print(f"The LCM of {a} and {b} is {mxno}.")
