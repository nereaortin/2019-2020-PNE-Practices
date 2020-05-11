#Session 7.Exercise 7

from Seq1 import Seq

print("-----| Practice 1, Exercise 7 |------")

#--null sequence
s1 = Seq()

# --valid sequence
s2 = Seq("ACTGA")

# --invalid sequence
s3 = Seq("Invalid sequence")

list = [s1, s2, s3]
for s in list:
    print("Sequence", list.index(s), ": (Lenght:", s.len(), ")", s)
    print("  Bases:", s.count())
    print("  Rev: ", s.reverse())