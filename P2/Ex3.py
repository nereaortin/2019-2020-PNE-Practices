from Client0 import Client


print(f"-----| Practice 2 Exercise 3 |------")

# -- Parameters of the server to talk to
IP = "212.168.111.134"
PORT = 8080

c = Client(IP, PORT)
print(c)

# -- Send a message to the server
print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")