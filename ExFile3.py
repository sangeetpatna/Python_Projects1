# 1) WAP to create a blank file after taking name of the file from user :
# filename=input("Enter the name of the file : ")
# fullname=(filename+".txt")
# file=open(fullname,"w")
# file.close()

# 1) WAP to create a blank file after taking name of the file from user :

# filename=input("Enter the name of the file : ")
# path="C:\\Users/Anant/Desktop/Ajooba\\"+filename+".txt"
# file=open(path,"w")
# file.close()

# 2) WAP to open the specified file and write the message in the file after taking input from user :
# file=input("Enter the name of the file : ")
# path="C:\\Users/Anant/Desktop/Ajooba\\"+file+".txt"
# myfile=open(path,"w")
# msg=input("Enter the message to add the in the file : ")
# myfile.write(msg)
# myfile.close()

# 2) WAP to open the specified file and print all message of the file on the screen :

# file=input("Enter the name of the file : ")
# path="C:\\Users/Anant/Desktop/Ajooba\\"+file+".txt"
# kuchbhi=open(path,"w")
# con=1
# while con==1:
#      msg=input("Enter the message you want to add in this file : ")
#      kuchbhi.write(msg)
#      kuchbhi.write("\n")
#      choice=input("Press y to continue writing : ")
#      if choice=='y' or choice=='Y':
#         con=1
#      else:
#         con=0
# kuchbhi.close()
        
# 3) WAP to open the specified file and print all messages of the file on the screen:

# filename=input ("Enter the name of the file you have to read : ")
# path="c:\\Users/Anant/Desktop/Ajooba\\"+filename+".txt"
# myfile=open(path,"r")
# data=myfile.read()
# print(data)
# myfile.close()

#4) WAP to open the specified file in such a way so the new message must be added after after the old content in the file:

# filename=input("Enter the name of the file to open : ")
# path="c:\\Users/Anant/Desktop/Ajooba\\"+filename+".txt"
# file=open(path,"a")
# con=1
# while con==1:
#     msg=input("Enter New message to add in this file : ")
#     file.write(msg)
#     file.write("\n")
#     choice=input("If you like to add something more press y otherwise n : ")
#     if choice=="y" or choice=="Y":
#         con=1
#     else:
#         con=0
# file.close()

# 5) WAP to create a copy of the specific file with a new name entered :

# sfname=input("Enter name of source file : ")
# dfname=input("Enter name of destination file : ")
# spath="c:\\Users/Anant/Desktop/Ajooba\\"+sfname+".txt"
# dpath="c:\\Users/Anant/Desktop/Ajooba\\"+dfname+".txt"
# sfile=open(spath,"r")
# dfile=open(dpath,"w")
# sdata=sfile.read()
# dfile.write(sdata)
# dfile.close()
# sfile.close()

# 6) WAP to check the file is writable or not :
# from os import *
# filename=input("Enter the name of the file : ")
# fullname="c:\\Users/Anant/Desktop/Ajooba\\"+filename+".txt"

# isExist=path.exists(fullname)
# if isExist:
#     print("This file exists.")
#     mfile=open(fullname.write())
#     if mfile:
#         print("file exists in writable format")
#     else:
#         print("file exists in readable format only")
# else:
#     print("This file doesn't exists.")
 
# 7) WAP to check the file exists or not :
   
# from os import *
# filename=input("Enter the name of the file : ")
# fullname="c:\\Users/Anant/Desktop/Ajooba\\"+filename+".txt"
# isExist=path.exists(fullname)
# if isExist:
#     print("This file exists.")
# else:
#     print("This file doesn't exists.")

# 8) WAP to take input of product name,qty,price and generate invoices. Also, save all the generated invoices as a new file by name of the customer :



# 9) WAP to generate an admission form and store as a new file by the name of the student :

# nos=input("Enter name of student : ")
# path="c:\\Users/Anant/Desktop/Ajooba\\"+nos+".txt"
# fn=input("Enter Father's Name : ")
# mn=int(input("Enter mob no. : "))
# eid=input("Enter Email-ID : ")
# add=input("Address : ")
# myfile=open(path,"w")
# myfile.write("\n")
# myfile.write("\t\t\t\tADMISSION FORM OF ")
# myfile.write(nos)
# myfile.write("\n")
# myfile.write("\n")
# myfile.write("Father's name \t\t:")
# myfile.write(fn)
# myfile.write("\n")
# myfile.write("Mobile NO. \t\t:")
# myfile.write(str(mn))
# myfile.write("\n")
# myfile.write("Email ID \t\t:")
# myfile.write(eid)
# myfile.write("\n")
# myfile.write("Address \t\t:")
# myfile.write(add)
# myfile.write("\n")
# myfile.close

# WAP to merge two files :

# sfname1=input("Enter name of source file1 : ")
# sfname2=input("Enter name of source file2 : ")
# dfname=input("Enter the destination file name : ")
# dfpath="c:\\Users/Anant/Desktop/Ajooba\\"+dfname+".txt"
# s1path="c:\\Users/Anant/Desktop/Ajooba\\"+sfname1+".txt"
# s2path="c:\\Users/Anant/Desktop/Ajooba\\"+sfname2+".txt"
# sfile1=open(s1path,"r")
# sfile2=open(s2path,"r")
# dfile=open(dfpath,"w")
# sdata1=sfile1.read()
# sdata2=sfile2.read()
# dfile.write(str(sdata1))
# dfile.write("\n")
# dfile.write(str(sdata2))
# dfile.write("\n")
# dfile.close()
# sfile1.close()
# sfile2.close()

