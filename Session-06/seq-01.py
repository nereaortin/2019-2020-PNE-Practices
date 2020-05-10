class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        self.strbases = strbases
        print("new sequence created")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


class Gene(Seq):
    #specialize class inside the main class Seq #inheritance #we can overwrite methods defined on class seq
    def __init__(self, strbases, name=""):
        super().__init__(strbases)
        self.name = name
        print("New gene created")
    def __str__(self):
        return self.name + "-" + self.strbases




#.. Main program
s1 = Seq("ATCGATC")
g = Gene("ACTTGA", "FRAT1")
print(f"sequence 1 : {s1}")
print(f"sequence 2 : {g}")

print(f"The length of the sequence 1 is {s1.len()}")
print(f"The length of the sequence 2 is {g.len()}")