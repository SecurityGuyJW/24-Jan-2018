import socket
import time
import threading

ip = "0.0.0.0"
port = 5001
memory = 1024

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conn.bind((ip, port))

conn.listen(2)

print("waiting for clients...")


def connEstablish(conn):
    client, netdata = conn.accept()

    response = client.recv(memory)

    print(response)

    print("client connected...")

    print("***enter 123 to terminate program***")

    try:
        client.send("Server Says:ACK!")
        msg = getMSG(client)
        print(msg)

    except socket.error as err:
        print(err)
        print("socket has been closed")
        client.close()

    return client


def connSession(client):
    try:
        sendMSG(client)
        getMSG(client)

    except client.error as err:
        print(err)
        print("server side socket closed...")
        client.close()

    client.close()

    while True:
        t_client, serv = client.accept()

        serverClientHandler = threading.Thread(target=connSession, args=(client,))

        serverClientHandler.start()


def sendMSG(conn):
    msg = raw_input("<server>:")

    str = "<server msg>:"

    msg = str + msg

    conn.send(msg)

    print("sending...")

    time.sleep(2)


def getMSG(conn):

    str = conn.recv(memory)

    print(str)


def connTerminate(client):
    print("chat-box program has ended succesfully...")
    client.close()


def main():
    client = connEstablish(conn)
    connSession(client)


main()
