# create a function. Take number input and reverse it.

def reverse_number():
    num = input("Enter Number: ")
    reverse = num[::-1]
    print(int(reverse))


reverse_number()