#--Session 4. Exercise 5

from pathlib import Path

FILENAME = "ADA.txt"
file_contents = Path(FILENAME).read_text()
data = file_contents.split('\n')

body = data[1:]
text = "".join(body)

print(len(body))