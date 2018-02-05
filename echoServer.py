import socket
import threading
import sys

ip = ''
port = 5005

conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

conn.bind((ip,port))

conn.listen(5)

print("listening for a connection")

def clientHandler(client):

    client.send("You are connected to the server!")
    client.send("Type xxx to terminate connection...")

    while True:
        msg = client.recv(1024)
        print("<client>>:%s"%msg)

        if msg == "xxx":
            break

        sendMsg = ("<server>:%s"%msg)
        client.send(sendMsg)

    client.close()

def threadedFunction(conn):

    while True:

        client,addr = conn.accept()

        beginClientThread = threading.Thread(target=clientHandler,args=(client,))
        beginClientThread.start()
        break

    conn.close()

threadedFunction(conn)

