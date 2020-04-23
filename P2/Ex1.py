from Client0 import Client, ping



print("-----| Practice 2 ","Exercise 1" , "|------")

# -- Parameters of the server to talk to
IP = "212.168.111.134"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

# -- Test the ping method
ping()

# -- Print the IP and PORTs
print(f"IP: {c.ip}, {c.port}")