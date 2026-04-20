# 👉 Create a class:
# class Student:
# 👉 Add:
# name
# age
# 👉 Create object and print values

class Student:
    School = "S.B.V. No.3"

    def __init__(self, name="Default", age="Default"):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, School: {self.School}"

# Case 1: With values
a = Student("Adarsh", 17)
print(a)

# Case 2: Without values (defaults will be used)
b = Student()
print(b)
