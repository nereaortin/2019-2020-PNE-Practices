#Session 5. Exercise 2

from Seq0 import * # We import the functions from Seq0.py

folder = "../session-04/" # Obtaining the gene files from this folder
filename = "U5.txt" #file we want to read

print("-----| Exercise 2 |------")
print("The first 20 bases are: ", seq_read_fasta(folder + filename)[:20])
# seq_read_fasta() function reads file and return content