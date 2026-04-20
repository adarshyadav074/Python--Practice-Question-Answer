# 👉 Use @staticmethod
# 👉 create function which prints greeting

class greet:
    @staticmethod
    def greet():
        name = input("Enter Name: ")
        print(f"Hello {name}")


greet.greet()