# Take a number
# print sum of its digits
# (123 → 6)

num = int(input("Enter a number: "))
sum_digits = 0

for digit in str(num):
    sum_digits += int(digit)

print("Sum of digits:", sum_digits)