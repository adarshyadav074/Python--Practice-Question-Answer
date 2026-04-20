# 👉 Check:
# 👉 age ≥18 AND citizen = "India"
# 👉 then "Eligible to vote"
a = int(input("Enter age: "))
b = input("Enter Citizenship: ").lower()

if a>=18 and b=="india":
    print("Eligible to vote.")
else:
    print("Not Eligible.")