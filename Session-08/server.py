#session-08.Exercise 4

import socket

# SERVER IP, PORT
PORT = 8080
IP = "192.168.1.115"

# -- Create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((IP, PORT))

s.listen(6)
while True:
    # accepting the request of the clients
    # clientsocket is the conexion
    (clientsocket, address) = s.accept()

    # read the message from the client
    # the server waits the message to arrive
    msg = clientsocket.recv(2080).decode("utf-8")
    print("Message from the client: {}".format(msg))

    #send a message
    message = "Hello from Nerea´s server"
    send_bytes = str.encode(message)
    # We must write bytes, not a string
    clientsocket.send(send_bytes)

    # Finish the connection
    clientsocket.close()