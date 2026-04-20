# 👉 Function:
# 👉 take 3 numbers → return maximum

def findmax():
    l = []
    n1 = int(input("Enter Number 1: "))
    l.append(n1)
    n2 = int(input("Enter Number 2: "))
    l.append(n2)
    n3 = int(input("Enter Number 3: "))
    l.append(n3)

    print(f"Max number is {max(l)}")

findmax()