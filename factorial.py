num=int(input("Enter the number : "))
def fon(num):
    if num==0:
        return 1
    else:
        return num*fon(num-1)
    
print (fon(num))