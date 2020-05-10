#Session 6.Exercise 3

class Seq:
    def __init__(self, strbases):
        self.strbases = strbases
        print("new sequence created")
        # passed as argument when creating the object

    def __str__(self):
        # shows the internal info of the object
        return self.strbases

    def len(self):
        # calculate the length of the sequence
        return len(self.strbases)


def print_seqs(list_seq): #this function receives a list of sequences/objects of class seq
    for i in list_seq:
        print("Sequence ", list_seq.index(i), "(Lenght: ", i.len(), ")", i)
#the function print_seqs() returns the index, length and the sequence itself


def generate_seqs(base, number):
    #this function returns a list with sequences where the pattern of bases is repeated from 1 to number
    new_seqlist= []
    for i in range(1, number + 1):
        new_seqlist.append(Seq(base * i))
    return new_seqlist


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)


#print()
print("List 2:")
print_seqs(seq_list2)