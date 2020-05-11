from Client0 import Client
from Seq1 import Seq


print(f"-----| Practice 2 Exercise 7 |------")

IP = "192.168.1.115"
PORT1 = 8081
PORT2 = 8082

FOLDER = "../Session-04/"
EXT = ".txt"
GENE = "FRAT1"

c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)

# Print the IP and PORTs
print(c1)
print(c2)

# Read the Gene from a file
s = Seq().read_fasta(FOLDER + GENE + EXT)
str_seq = str(s)

# Print the Gene
print(f"Gene {GENE}: {str_seq}")

lenght = 10

# first message to both servers
first_msg = f"Sending {GENE} Gene to the server, in fragments of {lenght} bases..."

c1.talk(first_msg)
c2.talk(first_msg)

# Create the fragments and sending them to both servers
for i in range(10):

    fragment = bases[i * 10:(i + 1) * 10]

    # Print on Client's console
    print(f"Fragment {i + 1}: {fragment}")

    # Message to send to the server
    msg = f"Fragment {i + 1}: {fragment}"

    # even fragments (counting from 0) are sent to server 1
    if i % 2:
        c2.talk(msg)

    # Odd segments are sent to server 2
    else:
        c1.talk(msg)