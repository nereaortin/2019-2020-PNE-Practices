from Client0 import Client


print(f"-----| Practice 2 Exercise 2 |------")

# -- Parameters of the server to talk to
IP = "212.168.111.134"
PORT = 8080

c = Client(IP, PORT)
print(c)