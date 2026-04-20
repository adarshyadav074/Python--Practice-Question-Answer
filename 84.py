# 👉 Create class Car:
# 👉 attributes:
# brand
# speed
# 👉 print details

class car:
    def __init__(self, Brand = "BMW", Speed = "310 km/h"):
        self.Brand = Brand
        self.Speed = Speed

    def __str__(self):
        return f"Brand = {self.Brand} and Speed = {self.Speed}"

a = car()
print(a)