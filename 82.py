# Find line number where "error" occurs

with open ("3.txt") as f:
    line = f.readlines()

for i in range(len(line)):
    if "error" in line[i].lower():
        print("Error found at line ",i+1)
        break
else:
    print("No Error Found.")