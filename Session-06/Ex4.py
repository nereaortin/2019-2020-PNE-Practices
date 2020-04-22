#Session 6. Exercise 4

import termcolor


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


def generate_seqs(base, number):
    #this function returns a list with sequences where the pattern of bases is repeated from 1 to number
    seq_list= []
    for i in range(1, number + 1):
        seq_list.append(Seq(base * i))
    return seq_list


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1", 'blue')
print_seqs(seq_list1, "blue")
print()
termcolor.cprint("List 2:", 'green')
print_seqs(seq_list2, "green")