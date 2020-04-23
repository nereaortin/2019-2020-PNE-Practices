import socket

# SERVER IP, PORT
PORT = 8080
IP = "212.168.111.134"

# -- Create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((IP, PORT))

s.listen(50)
while True:
    # accepting the request of the clients
    # clientsocket is the conexion
    (clientsocket, address) = s.accept()

    # read the message from the client
    # the server waits to the message to arrive
    m = clientsocket.recv(2100)

    print("Message from the client: ", end="")

    message = "Hello i am Nerea Ortín"
    send_bytes = str.encode(message)

    # We must write bytes, not a string
    clientsocket.send(send_bytes)

    # -- Finish the connection
    clientsocket.close()