#Session 5. Exercise 7
from Seq0 import *

folder = "../session-04/" # Obtaining the gene files from this folder
ext = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "U5"] # List of genes
gene = genes[0] #gene of the list we want


print("-----| Exercise 7 |------")

print("Gene", gene)
seq = seq_read_fasta(folder + gene + ext)[:20] #  .txt to read properly the file
complement = seq_complement(seq) # this function returns a complementary sequence
print("Frag: ", seq)
print("Com: ", complement)