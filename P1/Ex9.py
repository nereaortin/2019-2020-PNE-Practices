#Session 7. Exercise 9

from Seq1 import Seq

print("-----| Practice 1, Exercise 9 |------")


folder = "../Session-04/"
filename = folder + 'U5.txt'
s = Seq()
s.read_fasta(filename)

print("Sequence: (Lenght:", s.len(), ")", s)
print("  Bases:", s.count())
print("  Rev: ", s.reverse())
print("  Comp: ", s.complement())
