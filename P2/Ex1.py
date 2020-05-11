from Client0 import Client


print("-----| Practice 2 ","Exercise 1" , "|------")

# -- Parameters of the server we are connecting
IP = "192.168.1.115"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

# -- Test the ping method
c.ping()

# -- Print the IP and PORTs
print("IP:",c.ip,",",c.port)