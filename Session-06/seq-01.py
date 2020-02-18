class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        self.strbases = strbases
        print("new sequence created")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


class Gene(Seq):   #specialize class inside the main class (Seq)
    pass



#.. Main program
s1 = Seq("AACGTC")
g = Gene("ACCTGA")
print(f"sequence 1 : {s1}")    #con la f es como poner print("sequence 1:", s1)
print(f"sequence 2 : {g}")

print(f"The length of the sequence 1 is {s1.len()}")
print(f"The length of the sequence 2 is {g.len()}")