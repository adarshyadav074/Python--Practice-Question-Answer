# Program:
# take user input
# store in file
# read and print it

def hieeee():
    n = input("Enter Content: ")
    with open ("2.txt", "w") as f:
        f.write(n)

    with open ("2.txt", "r") as f:
        content = f.read()
        print(content)

hieeee()