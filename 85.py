# 👉 Add method:
# 👉 print student details

class Student:
    def __init__(self, Name, Age, Grade):
        self.Name = Name
        self.Age = Age
        self.Grade = Grade

    def __str__(self):
        return f"Name is {self.Name} and Age is {self.Age}.\nYou Got {self.Grade} Grade."
    
a = Student("Adarsh", 17, "A")
print(a)