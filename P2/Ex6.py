from Client0 import Client
from Seq1 import Seq


print(f"-----| Practice 2 Exercise 6 |------")

IP = "192.168.1.115"
PORT = 8080

FOLDER = "../Session-04/"
EXT = ".txt"
GENE = "FRAT1"

# Create a client object
c = Client(IP, PORT)

# Print the IP and PORTs
print(c)

# Read the Gene from a file
s = Seq().read_fasta(FOLDER + GENE + EXT)
str_seq = str(s)

lenght = 10
c.talk(f"Sending {GENE} Gene to the server, in fragments of {lenght} bases...")

for i in range(5):
    # 5 fragments of 10 bases each one
    fragment = str_seq[i * 10: (i + 1) * 10]

    # Print on Client's console
    print(f"Fragment {i + 1}: {fragment}")

    # Send the fragment to the server!
    c.talk(f"Fragment {i + 1}: {fragment}")