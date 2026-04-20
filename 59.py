# Calculate factorial of a number
n = int(input("Enter Number: "))

product = 1
for i in range(1,n+1):
    product = product * i

print(product)