# Read only first line of file

file_name = "1.txt"

with open (file_name, "r") as f:
    content = f.readline()
    print(content, end="")