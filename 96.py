# Write a code to check given number is Armstrong or not.

num = int(input("Enter a number: "))
sum_digits = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum_digits += digit ** 3   # cube of each digit
    temp //= 10

if num == sum_digits:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")