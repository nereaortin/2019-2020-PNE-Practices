from pathlib import Path

try:
    FILENAME = "RNU6_269P.txt"
    with open(FILENAME, "r") as f:
        file_contents = Path(FILENAME).read_text()
        header = next(f)
        for line in f:
            components = line.replace("\n", " ")
            print(components)
        f.close()
except FileNotFoundError:
    print("That file does not exist")