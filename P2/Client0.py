#Session 9.Exercise 0

import socket
import termcolor


class Client:

    def __init__(self, ip, port): #creates objects ip and port

        self.ip = ip
        self.port = port

    @staticmethod
    def ping():
        print("OK!")

    def __str__(self): #prints the objects ip and port
        return f"Connection to SERVER at {self.ip} , PORT: {self.port}"

    def talk(self, msg):
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))

        # Send data.
        s.send(str.encode(msg))

        # Receive data
        response = s.recv(2048).decode("utf-8")

        # Close the socket
        s.close()

        # Return the response
        return response

    def debug_talk(self, msg_client):
        msg_server = self.talk(msg_client)
        print("To Server:", end="")
        termcolor.cprint(msg_client, "blue")
        print("From Server: ", end="")
        termcolor.cprint(msg_server, "green")
        return msg_server