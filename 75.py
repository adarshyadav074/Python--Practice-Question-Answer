# 👉 Write a program:
# 👉 open a file and print its content

file_name = "1.txt"

with open (file_name, "r") as f:
    content = f.read()
    print(content)

# 👉 Open file using with statement
# 👉 print content
file_name = "1.txt"

with open (file_name, "r") as f:
    content = f.read()
    print(content)