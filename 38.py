# 👉 Create a dictionary:
# student = {
#     "name": "Adarsh",
#     "marks": 95,
#     "city": "Delhi"
# }

# 👉 Print:

# name
# marks

student = {
    "name": "Adarsh",
    "marks": 95,
    "city": "Delhi"
}

print(student["name"])
print(student["marks"])

# Add a new key: "age": 18

student["age"] = 17
print(student)

# Check if key "city" exists or not
print(student["city"]) 
if "city" in student:
    print("City Present in Student.")
else:
    print("City isn't Present.")