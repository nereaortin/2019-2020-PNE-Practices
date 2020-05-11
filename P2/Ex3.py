from Client0 import Client


print(f"-----| Practice 2 Exercise 3 |------")

# -- Parameters of the server we are connecting
IP = "192.168.1.115"
PORT = 8080

c = Client(IP, PORT)
print(c)

# -- Send a message to the server
print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")