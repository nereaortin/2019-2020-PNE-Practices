#Session 5. Exercise 8
from Seq0 import *

folder = "../session-04/" # Obtaining the gene files from this folder
ext = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "U5"] # List of genes
bases = ['A', 'C', 'T', 'G'] #list of bases

print("-----| Exercise 8 |------")


for name in genes:
    seq = seq_read_fasta(folder + name + ext) #  .txt to read properly the file
    dictionary = seq_count(seq) # dictionary with the number of apareance of each base
    value_list = list(dictionary.values()) #we create a list with each value obtained
    most_repeated = max(value_list) #we calculate which is the most repeated value
    print("Gene ", name, ": Most frequent Base:", bases[value_list.index(most_repeated)])