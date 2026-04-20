# print only odd Reverse table

# def table():
#     n = int(input("Enter Number: "))

#     for i in range(9, 0, -2):
#         print(f"{n} X {i} = {n*i}")

# table()

# print only Even Reverse table
# def table():
#     n = int(input("Enter Number: "))

#     for i in range(10, 0, -2):
#         print(f"{n} X {i} = {n*i}")

# table()

# print only odd table

# def table():
#     n = int(input("Enter Number: "))

#     for i in range(1, 10, 2):
#         print(f"{n} X {i} = {n*i}")

# table()

# Print Table but skip multiple of 3
def table():
    n = int(input("Enter Number: "))

    for i in range(1, 11):
        if i%3 == 0:
            continue
        else:
            print(f"{n} X {i} = {n*i}")

table()