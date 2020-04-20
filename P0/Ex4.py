#Session 5. Exercise 4
from Seq0 import *


folder = "../session-04/" # Obtaining the gene files from this folder
ext = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "U5"] # List of genes
bases = ['A', 'C', 'T', 'G'] # list of bases

print("-----| Exercise 4 |------")
for name in genes: # iterate throw the files in our list GENES
    seq = seq_read_fasta(folder + name + ext)
    print("Gene", name)
    for letter in bases:
        print(letter, ":", seq_count_base(seq, letter))
        # seq_count_base()  function that counts just one base