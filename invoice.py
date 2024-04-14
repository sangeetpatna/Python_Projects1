# this software application has been developed by team hubnet for Motabhai General Store
'''
in this application we are going to use of concept of the following components
1. function
2. data type and variable
3. file handling
'''
def printline(): #print definition
    print("--------------------------------------------------------------------------------")
printline() #function call
print("\t\t\tWelcome to Motabhai General Store")
printline()

# input section
noc=input("Enter Name of Customer : ")
nop=input("Enter Name of Product : ")
qop=int(input("Enter the quantity of product : ")) #str input to int conversion 
pop=int(input("Enter the price of product : ")) #str input to int conversion

#processing section
amount=qop*pop
gst=amount*18/100
pamt=amount+gst

#output section
printline()
print("\t\t\tInvoice of Mr. ",noc)
printline()
print("\t  NOP\t\tQty\t price\t Amount\t  Gst\t\tPayAmount")
print("\t",nop,"\t",qop,"\t",pop,"\t",amount,"\t",gst,"\t",pamt)
printline()
print("\t\t Thanks for Visiting!")
printline()
