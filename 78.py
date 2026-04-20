# Count number of lines in file.

file_name = "1.txt"

with open (file_name, "r") as f:
    lines = f.readlines()
    print(len(lines))