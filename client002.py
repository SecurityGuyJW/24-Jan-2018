# this client was written jan - 24 - 2018

import socket

conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def ipANDport(conn):

    data = list()

    ip = "192.168.0.42" #input("Enter IP:")
    port = 5000         #int(input("Enter Port:"))

    data.append(conn)
    data.append(ip)
    data.append(port)

    return data

def connConnect(netdata):

    try:
        netdata[0].connect((netdata[1],netdata[2]))

        netdata[0].send(bytes("hello from the client"))

        msg = netdata[0].recv(4060)

        print(msg)

    except socket.error as err:

        print(err)
        print("the connection was closed, port number can be reused")
        netdata[0].close()

def connTerminate(netdata):

    for i in netdata:
        print(i)
        print("\n")

    print("***socket has been terminated***")

    netdata[0].close()

def main():

    netdata = ipANDport(conn)

    connConnect(netdata)

    connTerminate(netdata)

main()
