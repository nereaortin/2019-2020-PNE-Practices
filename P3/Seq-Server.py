from Seq1 import Seq

import socket
import termcolor

# create the socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# to avoid a problem when a port is using

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP = "127.0.0.1"
PORT = 8080

# bind the socket to the servers ip and port

s.bind((IP, PORT))

# listen
s.listen()

print("Server is configured")

seq0 = "TAGCTAGCTAAGCTAAAGCTTGACTAGA"
seq1 = "ACTGACTAGTACGACTCAGCATAGTAGT"
seq2 = "ATGCATTTGACTAGCTAGCATAGAACAT"
seq3 = "ATTTGACATGCTTAGCTGACTAACCCAT"
seq4 = "GTCAGTCAGTCCTGCAGGATCGATCAGA"
list_seq = [seq0, seq1, seq2, seq3, seq4]

while True:
    # waiting for a client
    print("Waiting for a client connection")

    try:
        (cs, client_ip_port) = s.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")

        s.close()
        exit()

    else:

        # Read the message in bytes
        msg_raw = cs.recv(2048)

        # decode to read it properly
        msg = msg_raw.decode()

        li_command = msg.split(" ")
        command = li_command[0]

        if command == "PING":
            termcolor.cprint("PING command", 'green')
            print("OK!\n")

        elif command == "GET":
            termcolor.cprint("GET", 'green')

            if command[1] == "0":
                print(list_seq[0], "\n")
                response = list_seq[0]
                cs.send(response.encode())

            elif command[1] == "1":
                print(list_seq[1], "\n")
                response = list_seq[1]
                cs.send(response.encode())

            elif command[1] == "2":
                print(list_seq[2], "\n")
                response = list_seq[2]
                cs.send(response.encode())

            elif command[1] == "3":
                print(list_seq[3], "\n")
                response = list_seq[3]
                cs.send(response.encode())

            elif command[1] == "4":
                print(list_seq[4], "\n")
                response = list_seq[4]
                cs.send(response.encode())

        elif command[0] == "INFO":
            termcolor.cprint("INFO", 'green')

            sequence = Seq(li_command[1])
            print("Sequence: ", sequence)
            print("Total lenght: ", sequence.len())
            a_count = sequence.count_base('A')
            c_count = sequence.count_base('C')
            g_count = sequence.count_base('G')
            t_count = sequence.count_base('T')
            a_percent = (100 * a_count / sequence.len())
            c_percent = (100 * c_count / sequence.len())
            g_percent = (100 * g_count / sequence.len())
            t_percent = (100 * t_count / sequence.len())

            print("A:",a_count, "(", round(a_percent, 2), "%)")
            print("C:", c_count, "(", round(c_percent, 2), "%)")
            print("G:", g_count, "(", round(g_percent, 2), "%)")
            print("T:", t_count, "(", round(t_percent, 2), "%)")

            response = f"""Sequence: {sequence}
            Total length: {sequence.len()}
            A: {a_count} ({round(a_percent,2)}%)
            C: {c_count} ({round(c_percent,2)}%)
            G: {g_count} ({round(g_percent,2)}%)
            T: {t_count} ({round(t_percent,2)}%)"""
            cs.send(response.encode())

        elif command[0] == "COMP":
            termcolor.cprint("COMP", 'green')
            sequence = Seq(li_command[1])
            complement_seq = sequence.complement()
            print(complement_seq)
            cs.send(complement_seq.encode())


        elif command[0] == "REV":
            termcolor.cprint("REV", 'green')
            sequence = Seq(li_command[1])
            reverse_seq = sequence.reverse()
            cs.send(reverse_seq.encode())

        elif command[0] == "GENE":
            termcolor.cprint("GENE", 'green')
            gene = li_command[1]
            folder = "../session-04/"
            ext = ".txt"
            seq = read_fasta(folder + gene + ext)
            print(seq)
            cs.send(seq.encode())

        else:
            True
            cs.close()