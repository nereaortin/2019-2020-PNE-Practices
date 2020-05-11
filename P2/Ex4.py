from Client0 import Client


print(f"-----| Practice 2 Exercise 4|------")

# -- Parameters of the server we are connecting
#IP = "192.168.1.115"
PORT = 8080
IP = "127.0.0.1"

c = Client(IP, PORT)
print(c)

c.debug_talk("Message 1---")
c.debug_talk("Message 2: Testing !!!")

