#--Session 4. Exercise 4
from pathlib import Path


file_contents = Path("U5.txt").read_text()
data = file_contents.split('\n')

body = data[1:]
text = "\n".join(body)


print(f'the body of the print "U5.txt" file is:', text)
