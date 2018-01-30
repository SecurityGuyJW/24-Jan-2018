import socket
import time

memory = 1024


def connEstablish():
    ip = "172.17.79.148"

    port = 5001

    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    conn.connect((ip, port))

    conn.send("SYN!")

    response = conn.recv(memory)

    print(response)

    return conn


def connSessionStartEnd(conn):
    while True:

        try:
            sendMSG(conn)

            getMSG(conn)

        except socket.error as err:
            print(err)
            print("socket has been closed")
            conn.close()


def sendMSG(conn):
    msg = raw_input("<client>:")

    str = "<client msg>:"

    msg = str + msg

    conn.send(msg)

    print("sending...")

    time.sleep(2)

def getMSG(conn):

    time.sleep(2)

    str = conn.recv(memory)

    print(str)

    return str


def connTerminate(conn):
    print("chat-box has ended succesfully...")

    conn.close()


def main():
    conn = connEstablish()
    connSessionStartEnd(conn)


main()
