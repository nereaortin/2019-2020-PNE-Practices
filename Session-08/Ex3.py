#Session 8.Exercise 3

import socket

# SERVER IP, PORT
PORT = 8080
IP = "212.168.111.134"

while True:
  # -- Ask the user for the message
    msg = input("Enter the message: ")
  # -- Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # -- Establish the connection to the Server
    s.connect((IP, PORT))
  # -- Send the user message
    s.send(str.encode(msg))
  # -- Close the socket
    s.close()