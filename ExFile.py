# WAP to create a blank file after taking name of the file from user :
filename=input("Enter the name of the file : ")
fullname=(filename+".txt")
file=open(fullname,"w")
file.close()