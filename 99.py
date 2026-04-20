# Take a string
# count: vowels and consonants

def string():
    vovles = 0
    consonants = 0
    string = input("Enter String: ").lower()
    for i in string:
        if i.isalpha():
            if i in "aeiou":
                vovles += 1
            else:
                consonants += 1

    print("Vovles: ",vovles)
    print("Consonants: ",consonants)

string()