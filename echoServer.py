##########################################################################################################
#                                                                                                        #
# 1. socket and threading will be imported to perform the server roles in this script.                   #
#                                                                                                        #
#    a. The first role of the server is to recieve some data.                                            #
#                                                                                                        #
#    b. The second role is to send some data.                                                            #
#                                                                                                        #
#    c. The third role is to maintain a connection.                                                      #
#                                                                                                        #
#    d. The fourth role is to maintain multiple clients.                                                 #
#                                                                                                        #
#    e. Finally, the last role is to close the socket, and terminate the connection.                     #
#                                                                                                        #
# 2. the instance variables ip and port will be fed into the socket through the bind command.            #
#                                                                                                        #
# 3. The script will achieve multithreading by recursively calling clientHandler.                        #
#                                                                                                        #
# 4. The script will run each thread until the user types xxx or an error occurs.                        #
#                                                                                                        #
##########################################################################################################



import socket
import threading

ip = ''
port = 5000

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

