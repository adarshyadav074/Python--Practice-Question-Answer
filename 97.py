# Print numbers 1–50
# but:
# skip multiples of 5
# print only even numbers


for i in range(1, 51):
    if i % 2 == 0 and i % 5 != 0:
        print(i)
