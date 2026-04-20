# 👉 Create class:
# 👉 method to add two numbers

class add:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return f"The sum of both number is {self.num1 + self.num2}"
    
a = add(5, 50)
print(a)