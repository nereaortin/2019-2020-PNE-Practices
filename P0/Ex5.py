#Session 5. Exercise 5
from Seq0 import *

folder = "../session-04/"
ext = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "U5"]
bases = ['A', 'C', 'T', 'G']

print("-----| Exercise 5 |------")

for name in genes:
    seq = seq_read_fasta(folder + name + ext)
    print("Gene " + file, seq_count(sequence))
    # with this function we count the namber of bases in each folder