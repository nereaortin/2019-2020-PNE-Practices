#Session 6. Exercise 2

class Seq:
    def __init__(self, strbases):
        self.strbases = strbases
        # passed as argument when creating the object

    def __str__(self):
        # shows the internal info of the object
        return self.strbases

    def len(self):
        # calculate the length of the sequence
        return len(self.strbases)


def print_seqs(sequence): #this function receives a list of sequences
    for i in sequence:
        print("Sequence ", sequence.index(i), "(Lenght: ", i.len(), ")", i)
#the function print_seqs() returns the index, length and the sequence itseelf

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)