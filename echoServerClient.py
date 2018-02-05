import socket

conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

conn.connect(("192.168.237.160",5005))

def msgHandle(conn):

    try:
        while True:

            msg = conn.recv(1024)
            print(msg)
            msg = raw_input("<client>:")
            conn.send(msg)

            if msg == "xxx":
                print("client closed")
                conn.close()
                break

    except socket.error as err:

        print(err)

        socket.close()

msgHandle(conn)