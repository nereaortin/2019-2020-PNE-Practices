s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")


class Seq:
    """A class for representing sequence objects"""

    def __init__(self, strbases):
        self.strbases = strbases
        for element in s1:
            if element != "A" and element != "C" and element != "T" and element != "G":
                s1 = "ERROR!"
                print(s1)
        for element in s2:
            if element != "A" and element != "C" and element != "T" and element != "G":
                s2 = "ERROR!"
                print(s2)
        print("new sequence created")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)



print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")