from pathlib import Path #for reading fasta files of session 4


def valid_str(strbases):  # checks that all the elements in the seq are valid bases
    valid = ["A", "C", "G", "T"]
    for element in strbases:
        if element not in valid:  # if is an invalid base
            return False
    return True  # if is valid

class Seq:
    NULL = "NULL"
    ERROR = "ERROR"

    def __init__(self, strbases="NULL"):  # function __init__()for initializing the object
        # #always self to operate with the object
        if strbases == self.NULL:
            #create an object null
            print("NULL seq created")
            self.strbases = self.NULL
            return

        if not valid_str(strbases):
            #create an object invalid
            print("INVALID Seq!")
            self.strbases = self.ERROR
            return

        #this step is reached when the object is a string of valid bases
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):  # it run each time something is print
        return self.strbases  # it gives the internal info of the object

    def len(self):
        if self.strbases == self.NULL or self.strbases == self.ERROR: #returns length 0 for null and invalid
            return 0
        else:
            return len(self.strbases)


    def read_fasta(self, filename):
        content = Path(filename).read_text() #all the content of the file
        body = content.split('\n')[1:] #just the body of the file without the head
        self.strbases = "".join(body) #create an object with the body sequence

        return self

    def count_base(self, b):
        return self.strbases.count(b)

    def count(self):  # creates a dictionary with the count of each base in the seq
        dic_base = {'A': self.count_base('A'), 'T': self.count_base('T'),
             'C': self.count_base('C'), 'G': self.count_base('G')}

        return dic_base

    def reverse(self):#function that returns the reverse of only the valid seq
        if self.strbases == self.NULL:#for the null and invalid returns the object
            return "NULL"
        elif self.strbases == self.ERROR:
            return "ERROR"
        else:
            return self.strbases[::-1]

    def complement(self):
        dic_com = {"A": "T", 'T': 'A', 'C': 'G', 'G': 'C'}
        str_com = ""
        if self.strbases == self.NULL:
            return "NULL"
        elif self.strbases == self.ERROR:
            return "ERROR"
        else:
            for b in self.strbases:
                str_com += dic_com.get(b)
        return str_com
