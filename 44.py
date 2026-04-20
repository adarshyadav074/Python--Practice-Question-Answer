# Take age input:
# print:
# "Adult" (≥18)
# "Minor" (<18)

age = int(input("Enter age: "))

if age>18 or age==18:
    print("You're Adult.")
else:
    print("You're Minor.")