# Read file line by line using loop.

file_name = "1.txt"

with open (file_name, "r") as f:
    for line in f:
        print(line.strip())