#--Session 3. Exercise 3


from pathlib import Path

file = Path("dna.txt")

print("File: ", file)

text_dna = file.read_text()

print("Info: ", text_dna)

A = 0
G = 0
C = 0
T = 0
unknows = 0

for i in text_dna:
    if i == "A":
        A += 1
    elif i == "C":
        C += 1
    elif i == "G":
        G += 1
    elif i == "T":
        T += 1
    else:
        unknows += 1

print("Total length: ", len(text_dna))
print("A: ", A)
print("C: ", C)
print("G: ", G)
print("T: ", T)

print("unknows: ", unknows)