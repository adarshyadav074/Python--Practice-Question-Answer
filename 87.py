# 👉 Create class with __init__()
# 👉 initialize name & marks

class hiee:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name} got {self.marks} marks."
    
a = hiee("Adarsh", 549)
print(a)

# Create multiple objects with different values
b = hiee("Ritik", 339)
c = hiee("Abhimanyu", 335)
print(b)
print(c)