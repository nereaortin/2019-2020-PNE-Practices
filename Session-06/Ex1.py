#Session 6.Exercise 1
class Seq:
    def __init__(self, strbases):

        bases = ['A', 'C', 'G', 'T']

        for letter in strbases:
            if letter not in bases:
                print("ERROR!")
                self.strbases = "ERROR"
                return
        self.strbases = strbases # passed as argument when creating the object
        print("New sequence created!")  # method called every time a new object is created

    def __str__(self):
        return self.strbases# shows the info of the object

    def len(self):
        return len(self.strbases)#calculate the length of the sequence


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")