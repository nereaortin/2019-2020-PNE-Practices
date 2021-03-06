from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice 3, Exercise 7 |------")

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)
print(c)

#PING
print("* Testing PING...")
print(c.talk("PING"))

#GET
print("* Testing GET...")
for i in range(5):
    cmd = f"GET {i}"
    print(f"{cmd}: {c.talk(cmd)}", end="")

# INFO
seq = c.talk("GET 0")
print()
print("* Testing INFO...")
cmd = f"INFO {seq}"
print(c.talk(cmd))

# COMP
print(" Testing COMP...")
cmd = f"COMP {seq}"
print(cmd, end="")
print(c.talk(cmd))

# REV
print("* Testing REV...")
cmd = f"REV {seq}"
print(cmd, end="")
print(c.talk(cmd))

# GENE
print("* Testing GENE...")
for gene in ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]:
    cmd = f"GENE {gene}"
    print(cmd)
    print(c.talk(cmd))