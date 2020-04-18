#Session 4. Exercise 3

from pathlib import Path


FILENAME = "RNU6_269P.txt"
file_contents = Path(FILENAME).read_text()
data = file_contents.split('\n')
head = data[0]
print(head)



