#Session 7.Exercise 10

from Seq1 import Seq

print("-----| Practice 1, Exercise 10 |------")

folder = "../session-04/"
ext = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
bases = ['A', 'C', 'T', 'G']

for g in genes:
    str_folder = Seq().read_fasta(folder + g + ext)
    dictionary = str_folder.count()
    list_val = list(dictionary.values())
    most_common = max(list_val)
    print("Gene ", g, ": Most frequent Base:", bases[list_val.index(most_common)])