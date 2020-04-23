from Client0 import Client


print(f"-----| Practice 2 Exercise 4|------")

# -- Parameters of the server to talk to
IP = "10.9.27.156"
PORT = 8080

c = Client(IP, PORT)
print(c)

c.debug_talk("Message 1---")
c.debug_talk("Message 2: Testing !!!")