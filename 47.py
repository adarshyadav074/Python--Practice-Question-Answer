# 👉 Take username & password:
# 👉 check login:
# correct → "Login Success"
# wrong → "Invalid"

up = {"adarsh": "Aadu"}

a = input("Enter Username: ")
b = input("Enter Password: ")

# 👉 Proper login check
if a in up and up[a] == b:
    print("Login Success")
else:
    print("Invalid")