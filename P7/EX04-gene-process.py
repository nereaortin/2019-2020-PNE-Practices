import http.client
import termcolor
import json
from Seq1 import Seq

GENES = {
    'FRAT1': 'ENSG00000165879',
    'ADA': 'ENSG00000196839',
    'FXN': 'ENSG00000165060',
    'RNU6_269P': 'ENSG00000212379',
    'MIR633': 'ENSG00000207552',
    'TTTY4C': 'ENSG00000228296',
    'RBMY2YP': 'ENSG00000227633',
    'FGFR3': 'ENSG00000068078',
    'KDR': 'ENSG00000128052',
    'ANK2': 'ENSG00000145362',
}

gene = input("Write the gene name:")

BASES = ['A', 'T', 'C', 'G']

SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/'
ID = 'ENSG00000207552'
PARAM1 = '?type=genomic'
PARAM2 = '?content-type=application/json'
REQ = ENDPOINT + ID + PARAM2
URL = SERVER + ENDPOINT + ID + PARAM2

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", REQ)

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode()

# -- Create a variable with the data,
# -- form the JSON received
response = json.loads(data1)

termcolor.cprint("Gene", 'green', end="")
print(f": {gene}")
termcolor.cprint("Description", 'green', end="")
print(f": {response['desc']}")

seq = Seq(response['seq'])
print()


sl = seq.len()
ca = seq.count_base('A')
pa = "{:.1f}".format(100 * ca / sl)
cc = seq.count_base('C')
pc = "{:.1f}".format(100 * cc / sl)
cg = seq.count_base('G')
pg = "{:.1f}".format(100 * cg / sl)
ct = seq.count_base('T')
pt = "{:.1f}".format(100 * ct / sl)

termcolor.cprint("Total lengh", 'green', end="")
print(f": {sl}")

termcolor.cprint("A", 'blue', end="")
print(f": {ca} ({pa}%)")
termcolor.cprint("C", 'blue', end="")
print(f": {cc} ({pc}%)")
termcolor.cprint("G", 'blue', end="")
print(f": {cg} ({pg}%)")
termcolor.cprint("T", 'blue', end="")
print(f": {ct} ({pt}%)")

# -- Dictionary with the values
d = seq.count()

# -- Create a list with all the values
ll = list(d.values())

# -- Calculate the maximum
m = max(ll)

# -- Print the base
termcolor.cprint("Most frequent Base", 'green', end="")
print(f": {BASES[ll.index(m)]}")