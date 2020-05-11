from Client0 import Client
from Seq1 import Seq


print(f"-----| Practice 2 Exercise 5 |------")

IP = "192.168.1.115"
PORT = 8080

FOLDER = "../Session-04/"
EXT = ".txt"
GENE = "U5"

# Create a client object
c = Client(IP, PORT)

# Print the IP and PORTs
print(c)

# Read the Gene from a file
s = Seq().read_fasta(FOLDER + GENE + EXT)
str_seq = str(s)
# Sending
c.debug_talk(f"Sending {GENE} Gene to the server...")
c.debug_talk(str_seq)