# Take 5 numbers from user and store in list.
l = []
a = int(input("Enter Number 1: "))
l.append(a)
b = int(input("Enter Number 2: "))
l.append(b)
c = int(input("Enter Number 3: "))
l.append(c)
d = int(input("Enter Number 4: "))
l.append(d)
e = int(input("Enter Number 5: "))
l.append(e)

print(l)

# Find: maximum minimum

print(max(l))
print(min(l))

# Reverse a list
l.reverse()
print(l)