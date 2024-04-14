#for, while
#loop [action] : initilization, condition check, increment/decrement
'''
i=1             # initilization
while i<11:     # condtion check
    print(i)
    i+=1        # increment
'''
'''
for i in range(1,11,1):
    print(i)
'''
flag=1
add=0
while flag==1:
    num=int(input("Enter a Number : "))
    if num>0:
        add=add+num
        continue
    else:
        break
print("Sum of All Positive No : ",add)