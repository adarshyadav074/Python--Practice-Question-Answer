# Function:
# def greet(name="Guest"):

# 👉 test karo with and without argument
def greet(name="Guest"):
    print(f"Hello {name}")

greet()

def greet():
    name = input("Enter name: ")
    print(f"Hello {name}")

greet()