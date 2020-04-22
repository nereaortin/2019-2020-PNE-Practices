#Session 7.Exercise 10

from Seq1 import Seq

print("-----| Practice 1, Exercise 10 |------")

folder = "../session-04/"
ext = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269"]
bases = ['A', 'C', 'T', 'G']

for g in genes:
    se = Seq().seq_read_fasta(folder + g + ext)
    dictionary = se.count()
    lit = list(dictionary.values())
    most_common = max(lit)
    print("Gene ", g, ": Most frequent Base:", bases[lit.index(most_common)])