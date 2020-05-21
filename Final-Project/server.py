import http.server
import http.client
import socketserver
import termcolor
import json
from pathlib import Path
from Seq1 import Seq

#Servers port
PORT = 8080
server = "https://rest.ensembl.org"
IP = "localhost"


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True




final_message = f"""
    <a href="http://127.0.0.1:8080/">Main Page </a>
</body>
</html> """


def get_info(endpoint):

    try:
        conn.request("GET", endpoint + '?content-type=application/json')

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Read the response's body
    data1 = r1.read().decode()

    # -- Create a variable with the data from the JSON received
    info = json.loads(data1)
    return info


def get_sequence(id_gene):
    server4 = "rest.ensembl.org"
    endpoint = "/sequence/id"
    params = "/" + id_gene + "?content-type=application/json"
    conn = http.client.HTTPConnection(server4)

    try:
        conn.request("GET", endpoint + params)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    response = conn.getresponse()
    data1 = response.read().decode("utf-8")
    data = json.loads(data1)
    seq = data["seq"]
    return seq


def percentages(seq):
    count_bases = seq.count()
    length = seq.len()
    listvalues = list(count_bases.values())
    listt = []
    for value in listvalues:
        listt.append(f"{value} {round(value / length * 100), 2}%")
    listkeys = list(count_bases.keys())
    full_dictionary = dict(zip(listkeys, listt))
    return full_dictionary


def list_names(dict_species):
    counter = 0
    list_name = []
    while counter < int(len(dict_species)):
        animal = dict_species[counter]["common_name"]
        list_name.append(animal)
        counter += 1
    return list_name


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Open the form1.html file
        # Read the index from the file
        user_line = self.path #request_line por user_line

        if "json=1" in user_line:
            real_resource = user_line[:user_line.find("json=1") - 1]
            content_type = "application/json"
        else:
            real_resource = user_line #cambiar nombre real_resource
            content_type = "text/html"
        error_code = 200
        contents = ""
        line_path = real_resource.split('?') #list_resource por line_path
        verb = line_path[0] #resource por verb

        if verb == "/":
            contents_2 = Path("index-advanced.html").read_text()
            content_type = 'text/html'
            error_code = 200
        else:
            if verb == "/listSpecies":
                # First things to do
                limit_info = line_path[1] #line por limit_info
                limit_number = limit_info[limit_info.find("=") + 1:] #msg por limit_number
                # Getting the list of species
                path_endpoint = "/info/species?"
                a = get_info(path_endpoint)
                species = a["species"] #list_species por species
                list_species = list(species)
                number_species = len(list_species) #total_number por number_species
                # Seeing what is the number
                if limit_number == "":
                    number = number_species
                else:
                    number = limit_number
                contents =f"""
                            <!DOCTYPE html>
                            <html lang = "en">
                            <head>
                            <meta charset = "utf-8" >
                              <title> List of Species </title >
                            </head >
                            <body style="background-color: ligthgreen;">
                             The total number of species is: {number_species}
                             <br>
                             The limit you have selected is : {number} 
                             <br>
                             The names of the species are: 

                            </body>
                            </html>
                            """
                counter = 0
                list_animals = []

                if 0 < int(number) <= int(number_species):
                    # Viewing if it is json or not
                    while counter < int(number):
                        if "json=1" in user_line:
                            list_animals.append(list_species[counter]["animal_name"])
                            counter += 1
                            contents_2 = json.dumps({"species": list_animals})
                        else:
                            animal = list_species[counter]["animal_name"]
                            contents += f"<li> {animal} </li>"
                            counter += 1
                            contents_2 = contents + f"</ul>" + final_message
                    error_code = 200
                else:
                    contents = Path("Error.html").read_text()
                    error_code = 404
            elif verb == "/karyotype":
                # First things to do
                line = line_path[1]
                tittle = "KARYOTYPE OF A SPECIFIC SPECIE"
                sub_tittle = "Karyotype of a specie"
                index_eq = line.find("=")
                msg = line[index_eq + 1:]
                # Getting the list of species to prove if what you have writen exists
                ext1 = "/info/species?"
                ext2 = "/info/assembly/" + msg + "?"
                a = get_info(ext1)
                list_species = list(a["species"])
                list_species = list_names(list_species)
                if msg in list_species:
                    contents = f"""
                            <!DOCTYPE html>
                            <html lang = "en">
                            <head>
                            <meta charset = "utf-8" >
                              <title> List of Species </title >
                            </head >
                            <body style="background-color: ligthgreen;">
                             The total number of species is: {number_species}
                             <br>
                             The limit you have selected is : {number}
                             <br>
                             The names of the species are:

                            </body>
                            </html>
                            """
                    # Getting the info of the second endpoint
                    list_karyotype = get_info(ext2)
                    list_karyotype = list(list_karyotype["karyotype"])
                    contents += f"The names of the chromosomes of the specie: {str(msg)}  are: <br><ul>"
                    if "json=1" in user_line:
                        contents_2 = json.dumps({"karyotype": list_karyotype})
                    else:
                        for karyotype in list_karyotype:
                            contents += f" <li> {karyotype} </li>"
                        contents_2 = contents + f"</ul>" + final_message
                    error_code = 200
                else:
                    contents_2 = Path("Error.html").read_text()
                    error_code = 404
            elif verb == "/chromosomeLength":
                # First things to do
                line = line_path[1]
                tittle = "LENGTH OF THE SELECTED CHROMOSOME"
                sub_tittle = "Chromosome Length"
                index_1 = line.find("=")
                index_2 = line.find("&")
                specie = line[index_1 + 1: index_2]
                # Getting all the species to prove if the specie you have writen exists
                ext1 = "/info/species?"
                ext2 = "/info/assembly/" + specie + "?"
                a = get_info(ext1)
                list_species = list(a["species"])
                list_species = list_names(list_species)

                if specie in list_species:
                    number_1 = line[index_2:]
                    list_number = number_1.split("=")[1:]
                    number = 0
                    for n in list_number:
                        number = n
                    # Doing a list to prove if the chromosome exists
                    list_chromosome = get_info(ext2)
                    list_chromosome = list(list_chromosome["karyotype"])
                    if number in list_chromosome:
                        # Getting the info of the third endpoint
                        ext3 = "/info/assembly/" + specie + "/" + str(number) + "?"
                        length_final = get_info(ext3)
                        length = length_final["length"]
                        contents = html_folder(tittle, sub_tittle)
                        if "json=1" in user_line:
                            contents_2 = json.dumps({"length": str(length)})
                        else:
                            contents_2 = contents + f"The length of the chromosome {number} is {str(length)} " \
                                                 f"<br><br>" + final_message
                        error_code = 200
                    else:
                        contents_2 = Path("Error.html").read_text()
                        error_code = 404
                else:
                    contents_2 = Path("Error.html").read_text()
                    error_code = 404

            elif verb == "/geneSeq":
                try:
                    # First things to do
                    line = line_path[1]
                    tittle = "SEQUENCE OF A GENE"
                    sub_tittle = "The sequence of a human gene"
                    initial_index = line.find("=")
                    gene = line[initial_index + 1:]
                    # Getting the sequence of the gene
                    ext = "/xrefs/symbol/homo_sapiens/" + gene + "?"
                    id_gene = get_info(ext)
                    id_gene = id_gene[0]["id"]
                    sequence = get_sequence(id_gene)
                    contents_in = html_folder(tittle, sub_tittle)
                    contents_in += f"""The sequence of the gene {gene} is:<p><textarea rows = "20" cols= "100" 
                                style="background-color: lightpink;">{sequence}"""
                    # Viewing if it is json or not
                    if "json=1" in user_line:
                        contents_2 = json.dumps({"sequence": sequence})
                    else:
                        contents_2 = contents + f"</textarea></p>" + final_message
                    error_code = 200
                except requests.exceptions.HTTPError:
                    contents_2 = Path("Error.html").read_text()
                    error_code = 404

            elif verb == "/geneInfo":
                try:
                    # First things to do
                    line = line_path[1]
                    tittle = "INFO OF A GENE"
                    sub_tittle = "The information of a human gene"
                    contents = html_folder(tittle, sub_tittle)
                    initial_index = line.find("=")
                    gene = line[initial_index + 1:]
                    # Getting all the information of the endpoint geneInfo
                    ext = "/lookup/symbol/homo_sapiens/" + gene + "?"
                    decoded = get_info(ext)
                    start = decoded["start"]
                    end = decoded["end"]
                    chromosome = decoded["seq_region_name"]
                    id_gene = decoded["id"]
                    length_gene = end - start
                    # Viewing if it is json or not
                    if "json=1" in user_line:
                        dict_info = {"Start": start, "End": end, "Chromosome": chromosome,
                                     "Id": id_gene, "Length": length_gene}
                        contents_2 = json.dumps({"info": dict_info})
                    else:
                        contents += f"The gene gene  starts at  {str(start)}<br>The gene gene ends at {str(end)}" \
                                       f"<br>The gene gene is located at {str(chromosome)} chromosome<br>" \
                                       f"The id of the gene is:  {id_gene}<br>The length of the gene is: " \
                                       f"{str(length_gene)}<br><br>"
                        contents_2 = contents + final_message
                    error_code = 200
                except requests.exceptions.HTTPError:
                    contents_2 = Path("Error.html").read_text()
                    error_code = 404
            elif verb == "/geneCalc":
                try:
                    # First things to do
                    line = line_path[1]
                    tittle = "INFO OF A GENE"
                    sub_tittle = "The information of a human gene"
                    contents_in = html_folder(tittle, sub_tittle)
                    initial_index = line.find("=")
                    gene = line[initial_index + 1:]
                    # Getting the sequence
                    ext = "/xrefs/symbol/homo_sapiens/" + gene + "?"
                    id_gene = get_info(ext)
                    id_gene = id_gene[0]["id"]
                    s = get_sequence(id_gene)
                    # Using the Class
                    seq = Seq(s)
                    dict_sol = percentages(seq)
                    list_keys = list(dict_sol.keys())
                    list_values = list(dict_sol.values())
                    contents_in += f"The length of the gene is: {str(seq.len())} <br>Information about the bases<ul>"
                    # Viewing if it is json or not
                    if "json=1" in user_line:
                        list_keys.append("Length")
                        list_values.append(str(seq.len()))
                        final_dict = dict(zip(list_keys, list_values))
                        contents_2 = json.dumps({"Calc": final_dict})
                    else:
                        for n in list_keys:
                            index_base = list_keys.index(n)
                            contents += f"<li> Base:  {str(list_keys[index_base])}"
                            contents += f" --> {str(list_values[index_base])} </li>"
                        contents_2 = contents + f"</ul>" + final_message
                    error_code = 200
                except requests.exceptions.HTTPError:
                    contents_2 = Path("Error.html").read_text()
                    error_code = 404
            elif verb == "/geneList":
                try:
                    # First things to do
                    line = line_path[1]
                    tittle = "LIST OF GENES IN A RANGE"
                    sub_tittle = "All the genes in a specific range"
                    contents_in = html_folder(tittle, sub_tittle)
                    list_ = line.split("=")
                    index_a = list_[1].find("&")
                    chromosome = list_[1][:index_a]
                    index_b = list_[2].find("&")
                    start = list_[2][:index_b]
                    end = list_[3]
                    ext = "/overlap/region/human/" + chromosome + ":" + start + "-" + end + \
                          "?feature=gene;feature=transcript;feature=cds;feature=exon"
                    gene_list_ = get_info(ext)
                    contents_in += f"The genes in the range: {start} - {end} are: <br><br>"
                    # Viewing if it is json or not
                    if "json=1" in user_line:
                        list_keys = []
                        list_values = []
                        for n in gene_list_:
                            index = gene_list_.index(n)
                            list_keys.append(gene_list_[index]["id"])
                            if "external_name" in gene_list_[index]:
                                list_values.append(gene_list_[index]["external_name"])
                            else:
                                list_values.append("No name found")
                        final_dict = dict(zip(list_keys, list_values))
                        contents = json.dumps({"List": final_dict})
                    else:
                        for n in gene_list_:
                            index = gene_list_.index(n)
                            contents += f"""Gene: {gene_list_[index]["id"]}"""
                            if "external_name" in gene_list_[index]:
                                contents += f""" -->  {gene_list_[index]["external_name"]}<br>"""
                            else:
                                contents += f"<br>"
                        contents_2 = contents + final_message
                    error_code = 200
                except requests.exceptions.HTTPError:
                    contents_2 = Path("Error.html").read_text()
                    error_code = 404
        print(contents_2)

        self.send_response(error_code)
        # Define the content-type header:
        self.send_header('Content-Type', content_type)
        if "json=1" in user_line:
            encoded_dict = str(contents_2).encode('utf-8')
            # -- base64_dict = base64.b64encode(encoded_dict)
            self.send_header('Content-Length', len(encoded_dict))
            self.end_headers()
            self.wfile.write(encoded_dict)
        else:
            self.send_header('Content-Length', len(str.encode(contents_2)))
            self.end_headers()
            self.wfile.write(str.encode(contents_2))

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
        print("Stopped by the user")
        httpd.server_close()