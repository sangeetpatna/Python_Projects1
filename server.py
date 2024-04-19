from socket import *
server=socket()
server.bind (('localhost',9000))
server.listen(2)
print("waiting for client request...")
client,add=server.accept()
print("client connected : ",add)
client.send(bytes("Welcome to the World of Happiness!","utf-8"))
file=open("c:/Users/Anant/Desktop/ChatFilesForServer/serverChat.txt","a")
while True:
    sm=input("Server  : ")
    client.send(bytes(sm,"utf-8"))
    cm=client.recv(1024).decode()
    print("Client  : ",cm)
    file.write("\nServer msg : ")
    file.write(sm)
    file.write("\n")
    file.write("Client msg : ")
    file.write(cm)
    file.write("\n")
    if cm=="Bye" or cm=="bye":
        client.send(bytes("Bye","utf-8"))
        break
file.close()