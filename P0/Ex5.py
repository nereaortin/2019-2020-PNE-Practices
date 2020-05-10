#Session 5. Exercise 5
from Seq0 import *

folder = "../session-04/"
ext = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "U5"]
bases = ['A', 'C', 'T', 'G']

print("-----| Exercise 5 |------")

for name in genes:
    seq = seq_read_fasta(folder + name + ext)
    print("Gene " + name, seq_count(seq))
    # with this function we count the number of each bases in each folder