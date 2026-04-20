# s1 = {1, 2, 3}
# s2 = {3, 4, 5}

# 👉 Find:
# union
# intersection
s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s2.union(s1))
print(s1.intersection(s2))

# Check if element exists in set
if 3 in s1:
    print("3 is in s1.")
else:
    print("3 isn't present.")