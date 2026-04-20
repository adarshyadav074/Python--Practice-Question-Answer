# Write "Hello Adarsh" into a file

file_name = "2.txt"

with open (file_name, "w") as f:
    a = "Hello Adarsh"
    f.write(a)

# Append new line in existing file
b = "How are you??"
with open(file_name, "a") as f:
    f.write("\n" + b)

# Replace all content of file
c = "Hahaha, i gotch you."
with open (file_name, "w") as f:
    f.write(c)