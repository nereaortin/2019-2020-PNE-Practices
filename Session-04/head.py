
from pathlib import Path

try:
    FILENAME = "RNU6_269P.txt"
    with open(FILENAME, "r") as f:
        file_contents = Path(FILENAME).read_text()
        header = next(f)
        f.close()
    print(header)
except FileNotFoundError:
    print("That file does not exist")

