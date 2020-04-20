#Session 5.Exercise 6
from Seq0 import *

folder = "../session-04/" # Obtaining the gene files from this folder
ext = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "U5"] # List of genes
gene = genes[0] #gene of the list we want


print("-----| Exercise 6 |------")

print("Gene", gene)
seq = seq_read_fasta(folder + gene + ext)[:20] #  .txt to read properly the file for every gene folder
reverse = seq_reverse(seq) #with this function we change the seq order to the reverse
print("Frag: ", seq)
print("Rev: ", reverse)