import http.server
import socketserver
import termcolor
import json
import http.client
from pathlib import Path
from Seq1 import Seq

# Server's Port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# -- Server used for the project
server = 'rest.esembl.org'
params = '?content-type=application/json'

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # -- Print the request line
        termcolor.cprint(self.requestline, 'green')

        # -- Analyze the request line
        req_line = self.requestline.split(' ')

        # -- Get the path. It always start with the / symbol
        path = req_line[1]

        # --  Check all the arguments
        arguments = path.split('?')

        # -- The verb is located as the first argument
        verb = arguments[0]

        contents = Path('Error.html').read_text()
        status = 404

        # -- Gives a response depending of the existence of de
        if verb == '/':
            # Open index file (HTML)
            contents = Path('index.html').read_text()

        elif verb == '/listSpecies':
            # We extract the limit number entered by the user from the arguments:
            limit = arguments[1]

            # This endpoint lists all available species, their aliases, available adaptor groups and data release.
            endpoint = "info/species"

            try:

                # Connect with the server
                conn = http.client.HTTPConnection(server)

                # -- Send the request message, using the GET method. We are
                # -- requesting the main page (/)
                try:
                    conn.request("GET", endpoint + params)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                # -- Read the response message from the server
                response = conn.getresponse()

                # -- Print the status line
                print(f"Response received!: {response.status} {response.reason}\n")

                # -- Read the response's body:
                body = response.read().decode("utf-8")

                # -- We convert the body from string to dictionary:
                all_species_dict = json.loads(body)

                # -- We define the list of all species:
                all_species_list = []

                # -- We extract the display name of each species from the dictionary. Each species is a element of
                # -- a list, that is the value of a key called species.

                for k, v in all_species_dict.items():
                    if k == "species":
                        for element in v:
                            for k1, v1 in element.items():
                                if k1 == "display_name":
                                    species = v1

                                    # -- We add each species to the list:
                                    all_species_list.append(species)

                contents = f"""
                                           <!DOCTYPE html>
                                           <html lang = "en">
                                           <head>
                                           <meta charset = "utf-8" >
                                               <title>List of species</title >
                                           </head >
                                           <body>
                                           <p>The total number of species in ensembl is: {len(all_species_list)}</p>
                                           """

                # From limit, we extract the order and the value entered by the user:
                limit_action = limit.split("=")[0]
                limit_value = limit.split("=")[1]

                if limit_action == "limit":

                    # In case the user enters a limit value:
                    if limit_value != "":
                        contents += f"""<p>The number of species you selected are: {limit_value} </p>"""

                        # Invalid limit values:
                        if int(limit_value) > len(all_species_list) or int(limit_value) == 0 or int(
                                limit_value) < 0:
                            contents = f"""<!DOCTYPE html>
                                            <html lang = "en">
                                              <head>
                                                <meta charset = "utf-8" >
                                                <title>ERROR</title >
                                              </head>
                                                               <body>
                                                               <p>The limit you have introduced is out of range. Please, introduce a valid limit value</p>
                                                               </body></html>"""
                        else:
                            # We extract the first n species of the list, being n the limit ordered by the user.
                            limit_species_list = all_species_list[:(int(limit_value))]
                            contents += f"""<p>The species are: </p>"""
                            # The species are printed one by one:
                            for species in limit_species_list:
                                contents += f"""<p> - {species} </p>"""

                        contents += f"""<a href="/">Main page</a></body></html>"""

                    # In case the user does not enter any limit number, all the species will be displayed:
                    else:
                        contents += f"""<p>The number of species you selected is null, so all the species are displayed. </p>
                                                   <p>The species are: </p>"""

                        # The species are printed one by one:
                        for species in all_species_list:
                            contents += f"""<p> - {species} </p>"""
                        contents += f"""<a href="/">Main page</a></body></html>"""

                else:
                    contents = Path('Error.html').read_text()

            except ValueError:
                contents = f"""<!DOCTYPE html>
                                           <html lang = "en">
                                           <head>
                                            <meta charset = "utf-8" >
                                            <title>ERROR</title >
                                           </head>
                                           <body>
                                           <p>ERROR INVALID VALUE. Introduce an integer value for limit</p>
                                           <a href="/">Main page</a></body></html>"""

            # Karyotype: Return information about the karyotype of a specie: The name (usually a number) of all the
            # chromosomes:

            status = 200
        elif verb == '/karyotype':
            # -- HTML
            contents = f"""
                            <!DOCTYPE html>
                            <html lang = "en">
                            <head>
                            <meta charset = "utf-8" >
                              <title> GET </title >
                            </head >
                            <body>
                            <h2>Karyotype</h2>
                            <p>The names of the chromosomes are:</p>"""

            status = 200

        elif verb == '/chromosomeLength':
            # -- Get the argument to the right of the ? symbol
            pair = arguments[1]
            # -- Get all the pairs name = value
            pairs = pair.split('&')
            # -- Get the two elements: name and value
            s_name, spce = pairs[0].split('=')
            ch_index, chr = pairs[1].split('=')
            # -- Generate the html code
            contents = f"""
                                       <!DOCTYPE html>
                                       <html lang = "en">
                                       <head>
                                       <meta charset = "utf-8" >
                                         <title> GENE </title >
                                       </head >
                                       <body>
                                       <h2> Gene: {gene}</h2>
                                       <textarea readonly rows="20" cols="80"> {gene_str} </textarea>
                                       <br>
                                       <br>
                                       <a href="/">Main page</a>
                                       </body>
                                       </html>
                                       """
            status = 200
        elif verb == '/geneSeq':
            # -- Get the argument to the right of the ? symbol
            pair = arguments[1]
            # -- Get all the pairs name = value
            pairs = pair.split('&')
            # -- Get the two elements: name and value, and the operation name w/ the chosen operation
            name, seq = pairs[0].split('=')
            o_name, operation = pairs[1].split('=')
            seq = Seq(seq)
            if operation == 'Rev':
                result = seq.reverse()
            elif operation == 'Comp':
                result = seq.complement()
            else:
                # We calculate the length, amount of bases and the percentage they occupy in the sequence
                g_len = seq.len()
                counter = seq.count()
                per_a = 100 * int(counter['A']) / g_len
                per_c = 100 * int(counter['C']) / g_len
                per_t = 100 * int(counter['T']) / g_len
                per_g = 100 * int(counter['G']) / g_len
                result = f"""
                        <p>Total length: {g_len}</p>
                        <p>A: {counter['A']} ({per_a}%)</p>
                        <p>C: {counter['C']} ({per_c}%)</p>
                        <p>G: {counter['T']} ({per_t}%)</p>
                        <p>T: {counter['G']} ({per_g}%)</p>"""
            contents = f"""
                    <!DOCTYPE html>
                    <html lang = "en">
                    <head>
                    <meta charset = "utf-8" >
                        <title> Operations </title >
                    </head >
                    <body>
                    <h2> Seq:</h2>
                    <p>{seq}</p>
                    <h2> Operation: </h2>
                    <p>{operation}</p>
                    <h2> Result: </h2>
                    <p>{result}</p>
                    <br>
                    <br>
                    <a href="/">Main page</a>
                    </body>
                    </html>
                    """
            status = 200
        # -- Generating the response message
        self.send_response(status)

        # -- Define the content-type header:
        content_type = 'text/html'
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(contents.encode()))

        # -- The header is finished
        self.end_headers()

        # -- Send the response message
        self.wfile.write(contents.encode())

        return

    # ------------------------
    # - Server MAIN program
    # ------------------------
    # -- Set the new handler


Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('')
        print('Stopped by the user')
        httpd.server_close()