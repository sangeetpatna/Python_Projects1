# to calculate the exponential value of number m 
''' 
def pon(m,n):
    if n==0:
       return 1
    else:
       return m*pon(m,n-1)
   
print(pon(5,3))'''

# to find the square of the members of a list
# lll=[]

# def addEle():
#      l=int(input("Enter the members of the list :  " ))
#      lll.append(l)
# addEle()
# addEle()
# addEle()
# print(lll)
 
# for i in lll:
#    [print(i*i)]


# l=[1,2,3,4,5]
# print(l)
# for i in l:
#    [print(i*i)]
     
# ll=[12,4,55,15,23,20,14,18]
# print(list(filter(lambda n: n%2==0,ll)))
   
   
#to find the LCM of the given numbers:
# def calculate_lcm(x, y):  #(1,2)
#     # selecting the greater number  
#     if x > y:  
#         greater = x  
#     else:  
#         greater = y  
#     while(True):  
#         if((greater % x == 0) and (greater % y == 0)):  
#             lcm = greater  
#             break  
#         greater += 1  
#     return lcm    
  
# taking input from users  
# num1 = int(input("Enter first number: "))  
# num2 = int(input("Enter second number: "))  
# # printing the result for the users  
# print("The L.C.M. of", num1,"and", num2,"is", calculate_lcm(num1, num2)) 
    
# from math import *
# print(lcm (5,6,7))
# print( (7,8))

# def sob(a,b,c,d):
#       if a>b and a>c and a>d:
#          big=a
#       elif b>c and 
         
# def isPositive():
#    n=int(input("Enter the number : "))
#    if n>=0:
#       print ("yes the number is Non-negative")
#    else:
#       print ("No the number is negative")
# isPositive()

# def isLeapYear():
#    n=int(input("Enter the YEAR : "))
#    print(n)
#    if n%400==0 and n%100==0 or n%4==0 and n%100!=0:
#       print ("yes",n,"is a leap year" )
#    else:
#       print("No",n,"is not a leap year")
# isLeapYear()

# num=int(input("Enter a number : "))
# if num%2==0:
#    print (num,"is an even number.")
# else:
#    print(num,"is an odd number." )

# WAP for basic calculator

username="admin"
password="Admin@123"
UserId=input("Enter UserId : ")
pas=input("Enter")
fn=int(input("Enter first number : "))
sn=int(input("Enter second number : "))
op=input("Enter operator sign : ")[0]
if op=='+':
   print("Addition of ",fn,"and",sn,"is :",fn+sn)
elif op=='-':
   print("Subtraction of ",fn,"and",sn,"is :",fn-sn)
elif op==


