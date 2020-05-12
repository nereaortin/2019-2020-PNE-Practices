import http.client
import termcolor
import json

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
print(f": MRI633")
termcolor.cprint("Description", 'green', end="")
print(f": {response['desc']}")
termcolor.cprint("Bases", 'green', end="")
print(f": {response['seq']}")