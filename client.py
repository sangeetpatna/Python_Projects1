from socket import *
client=socket()
client.connect(('localhost',9000))
smsg=client.recv(1024).decode()
print("Server  : ",smsg)
file=open("c:/Users/Anant/Desktop/ChatFilesForClient/clientChat.txt","a")
while True:
    sm=client.recv(1024).decode()
    print("Server  : ",sm)
    cm=input("Client  : ")
    client.send(bytes(cm,"utf-8"))
    file.write("\nServer msg : ")
    file.write(sm)
    file.write("\n")
    file.write("Client msg : ")
    file.write(cm)
    file.write("\n")
    if cm=="Bye" or cm=="bye":
        sm=client.recv(1024).decode()
        print("Server  : ",sm)
        break
file.close()