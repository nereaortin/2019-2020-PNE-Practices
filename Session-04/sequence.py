from pathlib import Path

try:
    FILENAME = "ADA.txt"
    file_contents = Path(FILENAME).read_text()
    content = file_contents.split("\n")[1:]
    Body_file = ",".join(content).replace(",", "")
    print("Body of the U5.txt file:")
    print(len(Body_file))
except FileNotFoundError:
    print("That file does not exist")