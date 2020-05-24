# ------SERVER
import http.server
import socketserver
import termcolor
import json
import requests
import sys
import http.client
from pathlib import Path

# Servers port
PORT = 8080
server = "rest.ensembl.org"
connect = http.client.HTTPConnection(server)

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

# ----------------------------------------functions----------------------------------------------------


def data_dict(endpoint):
    # function that returns the info asked from a given endpoint
    try:
        connect.request("GET", endpoint + 'content-type=application/json')

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- Read the response message from the server
    r1 = connect.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    data1 = r1.read().decode()

    # -- Create a variable with the species data from the JSON received
    info = json.loads(data1)
    return info


def get_seq(id):
    # function that returns the sequence of a gene, knowing its id
    endpoint = "/sequence/id/"
    parameters = id + "?content-type=application/json"

    try:
        connect.request("GET", endpoint + parameters)

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- Read the response message from the server
    r1 = connect.getresponse()

    # -- Read the response's body
    data1 = r1.read().decode()

    # -- Create a variable with the data,
    # -- form the JSON received
    sequence = json.loads(data1)["seq"]
    return sequence


def bases_percent(sequence):
    # function that given a sequence returns a dictionary with the percent of each base
    bases = ['A', 'C', 'T', 'G']
    # create a new list to append the percentages
    list_percent = []
    for element in bases:
        # for each base, calculate the percentage in the gene sequence
        percentage = round(sequence.count(element) * 100 / len(sequence), 2)
        list_percent.append(percentage)
    values = dict(zip(bases, list_percent))
    return values


def json_request(line):
    # function checks for request of a json file, and removes 'json=1' to work with the request line properly
    if 'json=1' in line:
        # if is json request: we remove 'json=1' from the request line
        user_request = line[:line.find("json=1") - 1]
    elif 'json=1' not in line:
        # if this is not a json request: all the path is our request
        user_request = line

    return user_request

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line in green
        termcolor.cprint(self.requestline, 'green')

        # Read the index from the file
        request_line = self.requestline.split(" ")

        # Take the symbol / out of the path
        path_req = request_line[1]

        error_code = 200
        # returns the request line without json, if there is
        path = json_request(path_req)

        # we separate the endpoint from the rest of the parameters
        line_path = path.split('?')
        verb = line_path[0]
# -------------------------------------------BASIC LEVEL----------------------------------------------------------

        # main page endpoint--> returns an html page with the index
        if verb == "/":
            contents = Path("index.html").read_text()
            error_code = 200

        # listSpecies endpoint--> with a given limit, returns all the species to show
        elif verb == "/listSpecies":
            path_endpoint = "/info/species?"
            # we take the part of the line with the parameters
            line = line_path[1]
            try:
                # obtain the limit number from the path
                limit_number = line[line.find("=") + 1:]
                # get from the dictionary obtain from this endpoint the values for 'species'
                info = data_dict(path_endpoint)["species"]
                # create a list with this values and calculate its length
                list_species = list(info)
                number_species = len(list_species)
                # if the user does not enter a limit we suppose that wants all the species
                if limit_number == "":
                    num = number_species
                else:
                    num = int(limit_number)
                    # create the html file
                contents = f"""
                                       <!DOCTYPE html>
                                       <html lang = "en">
                                       <head>
                                       <meta charset = "utf-8" >
                                         <title> List of Species </title >
                                       </head >
                                       <body style="background-color: lightgreen;">
                                        The total number of species in the ensemble is: {number_species}
                                        <br>
                                        The limit you have selected is : {num} 
                                        <br>
                                        The name of the species are: 

                                       </body>
                                       </html>
                                       """
                count = 0
                total_species = []

                if "json=1" in path_req:
                    while num > count:
                        # create a dictionary containing a list with the names of the species in json file
                        name = list_species[count]["display_name"]
                        total_species.append(name)
                        count += 1
                    contents = json.dumps({"species": total_species})
                else:
                    while num > count:
                        # add each specie to the contents of the html page until the limit num is reached
                        name = list_species[count]["display_name"]
                        contents += f"<i><li> {name} </li></i>"
                        count += 1
                contents += f"""<br><br><br><a href="/">Main page</a>"""
            except ValueError:
                # this exception is reached when the specie is not in the data base
                contents = Path('Error.html').read_text()
                error_code = 404
            except LookupError:
                # this exception is reached when the specie is not in the data base
                contents = Path('Error.html').read_text()
                error_code = 404

        # Karyotype endpoint--> with a given specie, returns all the chromosomes name of that specie
        elif verb == "/karyotype":
            path_endpoint = "/info/assembly/"
            # we take the part of the line with the parameters
            line = line_path[1]
            # obtain the specie name from the path
            name = line[line.find("=") + 1:]
            try:
                # get from the dictionary obtain from this endpoint the values for 'karyotype'
                endpoint = path_endpoint + name + "?"
                info = data_dict(endpoint)["karyotype"]
                # we create a list with the values for the karyotype obtained
                list_chromosome = list(info)
                # create the html file
                contents = f"""
                            <!DOCTYPE html>
                            <html lang = "en">
                            <head>
                            <meta charset = "utf-8" >
                              <title> Karyotype </title >
                            </head >
                            <body style="background-color:peachpuff ;">
                            The names of the chromosomes are:


                            </body>
                            </html>
                            """

                if "json=1" in path_req:
                    # create a dictionary containing a list with the names chromosomes in json file
                    contents = json.dumps({"karyotype": list_chromosome})
                else:
                    for element in list_chromosome:
                        # add each chromosome name to the contents of the html page
                        contents += f"<p> {str(element)} </p>"
                    contents += f"""<br><br><br><a href="/">Main page</a>"""
                error_code = 200
            except ValueError:
                # this exception is reached when the specie is not in the data base
                contents = Path('Error.html').read_text()
                error_code = 404
            except LookupError:
                # this exception is reached when the specie is not in the data base
                contents = Path('Error.html').read_text()
                error_code = 404

        # chromosomeLength endpoint--> with a given specie and chromosome, returns its length
        elif verb == "/chromosomeLength":
            path_endpoint = '/info/assembly/'
            # we take the part of the line with the parameters
            line = line_path[1]
            # separate the two parameters that are joined with a '&'
            line_endpoint = line.split("&")
            # get the values for the parameters situated after the '='
            line_specie = line_endpoint[0].split("=")
            line_chromo = line_endpoint[1].split("=")
            specie = line_specie[1]
            chromo = line_chromo[1]
            try:
                endpoint = path_endpoint + specie + "/" + chromo + "?"
                # create the html file
                contents = f"""
                                                    <!DOCTYPE html>
                                                    <html lang = "en">
                                                    <head>
                                                    <meta charset = "utf-8" >
                                                      <title> Chromosome Length </title >
                                                    </head >
                                                    <body style="background-color:plum">

                                                    </body>
                                                    </html>
                                                    """

                # get from the dictionary obtain from this endpoint the value for 'length'
                info = data_dict(endpoint)["length"]
                length = str(info)
                if "json=1" in path_req:
                    # create a dictionary containing the length of the chromosome of the specie selected in json file
                    contents = json.dumps({"length": length})
                else:
                    # add the length of the chromo of the specie selected to the contents of the html page
                    contents += f"""<i> The length of the chromosome is: {length} </i> <br><br><br>
                                    <a href="/">Main page</a>"""
            except ValueError:
                # this exception is reached when the length is not in the data base
                contents = Path("Error.html").read_text()
                error_code = 404
            except LookupError:
                # this exception is reached when the length is not in the data base
                contents = Path("Error.html").read_text()
                error_code = 404
# ------------------------------------------------MEDIUM LEVEL---------------------------------------------------------
        # geneSeq endpoint--> with a given gene, it returns all its sequence
        elif verb == "/geneSeq":
            path_endpoint = "/xrefs/symbol/homo_sapiens/"
            # we take the part of the line with the parameters
            line = line_path[1]
            # obtain the number of the gene from the path
            gene = line[line.find("=") + 1:]
            endpoint = path_endpoint + gene + "?"
            # create the html file
            contents = f"""
                                        <!DOCTYPE html>
                                        <html lang = "en">
                                        <head>
                                        <meta charset = "utf-8" >
                                          <title> Gene sequence </title >
                                        </head >
                                        <body style="background-color:darkseagreen ;">

                                        </body>
                                        </html>
                                         """
            try:
                # get from the dictionary obtain from this endpoint the value of the id of the gene
                info = data_dict(endpoint)
                gene_id = info[0]["id"]
                # call the function get_seq(), where introducing the id returns the sequence of this gene
                gene_seq = get_seq(gene_id)
                # add the sequence of the gene selected to the contents of the html page
                contents += f"""<h3> The sequence of {gene} gene is: </h3><p><textarea rows = "40" cols= "140" 
                                style="background-color: darksalmon;"><p>{gene_seq} </p>
                                </textarea></p><br><br><br><a href="/">Main page</a>"""
                if "json=1" in path_req:
                    # create a dictionary containing the sequence of the gene selected in json file
                    contents = json.dumps({"sequence": gene_seq})
                error_code = 200
            except ValueError:
                # this exception is reached when the gene you selected is not in the data base
                contents = Path("Error.html").read_text()
                error_code = 404
            except LookupError:
                # this exception is reached when the gene you selected is not in the data base
                contents = Path("Error.html").read_text()
                error_code = 404

        # geneInfo endpoint--> with a given gene, it returns information about it
        elif verb == "/geneInfo":
            path_endpoint = '/lookup/id/'
            # we take the part of the line with the parameters
            line = line_path[1]
            # obtain the number of the gene from the path
            gene = line[line.find("=")+1:]
            endpoint = "/xrefs/symbol/homo_sapiens/" + gene + "?"
            # create the html file
            contents = f"""
                                                <!DOCTYPE html>
                                                <html lang = "en">
                                                <head>
                                                <meta charset = "utf-8" >
                                                  <title> Gene sequence </title >
                                                </head >
                                                <body style="background-color:coral;">

                                                </body>
                                                </html>
                                                 """
            try:
                # get from the dictionary obtain from this endpoint the value of the id of the gene
                info = data_dict(endpoint)
                gene_id = info[0]["id"]
                endpoint = path_endpoint + gene_id + "?"
                # call the function get_seq(), where introducing the id returns the sequence of this gene
                gene_seq = get_seq(gene_id)
                # calculate the length of this sequence
                length = len(gene_seq)
                # get from the dictionary obtain from this endpoint the value of the point of start, end and the chromo
                data = data_dict(endpoint)
                start = data["start"]
                end = data["end"]
                chromosome = data["seq_region_name"]

                if "json=1" in path_req:
                    # create a dictionary containing the information of the gene in json file
                    contents = json.dumps({"information": {"Start": start, "End": end, "Length": length,
                                           "ID": gene_id, "Chromosome": chromosome}})
                else:
                    # add the information of the gene selected(start, end, len, id and chromo) to the html page
                    contents += f"""<h3>Information about the {gene} human gene:</h3>
                                    <p>Point of start: {start}</p>
                                    <p>Point of end: {end}</p>
                                    <p>Length: {length}</p>
                                    <p> ID of the gene: {gene_id}</p>
                                    <p>Chromosome location: {chromosome}</p>
                                    <br><br><br><a href="/">Main page</a>
                                   """
                error_code = 200
            except ValueError:
                # this exception is reached when the gene you selected is not in the data base
                contents = Path("Error.html").read_text()
                error_code = 404
            except LookupError:
                # this exception is reached when the gene you selected is not in the data base
                contents = Path("Error.html").read_text()
                error_code = 404

        # geneCalc endpoint--> with a given gene, it returns information about it
        elif verb == "/geneCalc":
            # we take the part of the line with the parameters
            line = line_path[1]
            # obtain the number of the gene from the path
            gene = line[line.find("=") + 1:]
            # define the endpoint where we are taking the info
            endpoint = "/xrefs/symbol/homo_sapiens/" + gene + "?"
            try:
                # get from the dictionary obtain from this endpoint the value of the id of the gene
                info = data_dict(endpoint)
                gene_id = info[0]["id"]
                # call the function get_seq(), where introducing the id returns the sequence of this gene
                gene_seq = get_seq(gene_id)
                # calculate the length of this sequence
                length = len(gene_seq)
                # call the function bases_percent(), where with the seq of the gene it calculates the % of each base
                dict_percent = bases_percent(gene_seq)
                # create the html file
                contents = f"""
                         <!DOCTYPE html>
                         <html lang = "en">
                         <head>
                         <meta charset = "utf-8" >
                         <title> Gene calculations </title >
                         </head >
                         <body style="background-color:lightblue;">

                         <h3>Calculations on human gene</h3>
                         <p>The length of the {gene} gene is: {length} and the calculations are:</p>
                          </body>
                          </html>
                          """

                error_code = 200
                if "json=1" in path_req:
                    # create dictionary containing a list with calculations on the gene selected, to create json file
                    list_data = []
                    for n, i in dict_percent.items():
                        data = f"""{n}: {gene_seq.count(n)} ({i}%)"""
                        list_data.append(data)
                    contents = json.dumps({"Calc": list_data})
                else:
                    # add the calculations of the gene selected to the html page
                    for n, i in dict_percent.items():
                        contents += f"""<p>{n}: {gene_seq.count(n)} ({i}%) </p>"""
                    contents += f"""<br><br><br><a href="/">Main page</a></body></html>"""
            except ValueError:
                # this exception is reached when the gene you selected is not in the data base
                contents = Path("Error.html").read_text()
                error_code = 404
            except LookupError:
                # this exception is reached when the gene you selected is not in the data base
                contents = Path("Error.html").read_text()
                error_code = 404

        # geneList endpoint--> with a given chromosome, start and end, it returns the genes located in this fragment
        elif verb == "/geneList":
            path_endpoint = "/overlap/region/human/"
            # we take the part of the line with the parameters
            line = line_path[1]
            # separate the 3 given parameters that are separated with '&'
            data = line.split("&")
            try:
                # we take the parameters entered by the user that are located after '='
                index_1 = data[0].find("=")
                index_2 = data[1].find("=")
                index_3 = data[2].find("=")
                chromosome = data[0][index_1 + 1:]
                start = data[1][index_2 + 1:]
                end = data[2][index_3 + 1:]
                params = "?feature=gene;content-type=application/json"
                # define the endpoint where we are taking the info
                endpoint = path_endpoint + chromosome + ":" + start + "-" + end + params
                # create the html file
                contents = f"""
                                                     <!DOCTYPE html>
                                                     <html lang = "en">
                                                     <head>
                                                     <meta charset = "utf-8" >
                                                     <title> Gene List</title >
                                                     </head >
                                                    <body style="background-color:lightblue;">
                                                     <h3>Genes located in the {chromosome} chromosome:</h3>
                                                     <h4>From {start} to {end} are:</h4>

                                                     </body>
                                                     </html>
                                                     """

                # get a list of dictionaries with the genes obtain around this fraction
                r = requests.get("https://rest.ensembl.org" + endpoint, headers={"Content-Type": "application/json"})

                if not r.ok:
                    r.raise_for_status()
                    sys.exit()

                info = r.json()

                # create a list with all the genes around this fraction
                list_gene = []
                for i in info:
                    list_gene.append(i["external_name"])
                if "json=1" in path_req:
                    # create a dictionary containing a list with genes that are on this fraction, to create json file
                    contents = json.dumps({"List": list_gene})
                else:
                    # add the genes of the fraction of the chromosome selected to the html page
                    for i in list_gene:
                        contents += f"""<li>{i}</li>"""
                    contents += f"""<br><br><br><a href="/">Main page</a></body></html>"""
                error_code = 200
            except ValueError:
                # this exception is reached when the fraction of chromosome you selected is not valid
                contents = Path("Error.html").read_text()
                error_code = 404
            except LookupError:
                # this exception is reached when the fraction of chromosome you selected is not valid
                contents = Path("Error.html").read_text()
                error_code = 404
            except requests.exceptions.HTTPError:
                # this exception is reached when the fraction of chromosome you selected is not valid
                contents = Path("Error.html").read_text()
                error_code = 404

        print(contents)

        self.send_response(error_code)
        if "json=1" in path_req:
            self.send_header('Content-Type', "application/json")
            data_encode = str(contents).encode('utf-8')
            self.send_header('Content-Length', len(data_encode))
            self.end_headers()
            self.wfile.write(data_encode)
        else:
            self.send_header('Content-Type', "text/html")
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()
            self.wfile.write(str.encode(contents))

        return

    # ------------------------
    # - Server MAIN program
    # ------------------------
    # -- Set the new handler


Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
