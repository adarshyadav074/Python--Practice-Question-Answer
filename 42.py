# 👉 Program:
# Take 5 names
# store in dictionary
# assign random marks
# print topper

import random

dict = {}

a = input("Enter Name: ")
dict[a]= random.randint(1,100)
b = input("Enter Name: ")
dict[b] = random.randint(1,100)
c = input("Enter Name: ")
dict[c] = random.randint(1,100)
d = input("Enter Name: ")
dict[d] = random.randint(1,100)
e = input("Enter Name: ")
dict[e] = random.randint(1,100)


print(dict)

print(f"Topper is {max(dict)}.")