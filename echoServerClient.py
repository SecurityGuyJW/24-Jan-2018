##########################################################################################################
#                                                                                                        #
# 1. socket library will be used to connect to a server.                                                 #
#                                                                                                        #
#    a. The first role of the client is to connect to a server                                           #
#                                                                                                        #
#    b. The second role is to send some data.                                                            #
#                                                                                                        #
#    c. The third role is to recieve some date.                                                          #
#                                                                                                        #
#    d. The fourth role is to display the messages.                                                      #
#                                                                                                        #
#    e. Finally, the last role is to send the command to terminate server and client connection.         #
#                                                                                                        #
# 2. The instance variables ip and port will be fed into the socket through the connect command.         #
#                                                                                                        #
#     a. The ip instance variable need to be changed to the current host IP address.                     # 
#                                                                                                        #
#     b. The port needs to be changed into any closed port in the system (try 5000).                     #
#                                                                                                        #
#     c. Once this is done verify that the port on the server is the same as the port on the client.     #
#                                                                                                        #
# 3. Once you are satifies with the echo functionality type xxx.                                         #
#                                                                                                        #
##########################################################################################################

import socket

ip = "192.168.237.160"
port = "5000"

conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

conn.connect((ip,port))

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
