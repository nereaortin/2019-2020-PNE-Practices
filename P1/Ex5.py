#Session 7.Exercise 5

from Seq1 import Seq

print("-----| Practice 1, Exercise 5 |------")

#--null sequence
s1 = Seq()

# --valid sequence
s2 = Seq("ACTGA")

# --invalid sequence
s3 = Seq("Invalid sequence")

list= [s1, s2, s3]

for s in list:
    print("Sequence", list.index(s),": (Lenght:", s.len(),")", s)
    for b in ['A', 'C', 'T', 'G']:
        print(b,":",s.count_base(b), end=", ")
    print()