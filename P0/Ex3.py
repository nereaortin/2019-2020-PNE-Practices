from Seq0 import *

FOLDER = "../session-04/" # Obtaining the gene files from this folder
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "U5"] # List of genes

print("-----| Exercise 3 |------")

for name in GENES:  # iterate throw the files in our list GENES
    seq = seq_read_fasta(FOLDER + name + EXT) #  .txt to read properly the file and seq_read_fasta() to obtain the body
    print("Gene ", name, "---> Lenght: ", seq_len(seq)) # returns the length of each gene folder