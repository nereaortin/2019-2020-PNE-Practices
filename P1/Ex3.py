#Session 7.Exercise 3

from Seq1 import Seq

print("-----| Practice 1, Exercise 3 |------")
# we are creating sequences passing a string with the bases to an object
# null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

print("Sequence 1: ", s1)
print("Sequence 2: ", s2)
print("Sequence 3: ", s3)