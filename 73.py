# 👉 Write recursive function:
# 👉 sum of first n natural numbers

def find_sum(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n + find_sum(n-1)
    
n = int(input("Enter Number: "))
print(f"The sum of {n} is {find_sum(n)}")