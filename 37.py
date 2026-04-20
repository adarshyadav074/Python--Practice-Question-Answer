# Create a tuple:
# t = (1, 2, 3, 2, 4)

# 👉 Count how many times 2 appears.

t = (1, 2, 3, 2, 4)

print(t.count(2))

# Find index of first occurrence
# 1 = 0
# 2 = 1
# 3 = 2
# 2 = 3
# 4 = 4

# Try to change tuple value and observe error
t[3] = 8 # Tuples are immutable we cannot change a value in tuple.
