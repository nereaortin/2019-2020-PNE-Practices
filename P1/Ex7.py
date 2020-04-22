#Session 7.Exercise 7

from Ex1 import Seq

print("-----| Practice 1, Exercise 7 |------")

#--null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

for i, s in enumerate([s1, s2, s3]):
    print("Sequence", i, ": (Lenght:", s.len(), ")", s)
    print("  Bases:", s.count())
    print("  Rev: ", s.seq_reverse())