# 👉 Function:
# 👉 print multiplication table of a number

def mul():
    n = int(input("Enter Number: "))

    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")

mul()