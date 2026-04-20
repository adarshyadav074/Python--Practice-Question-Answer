# 100 Special
# Guess the number game: User guess number.

import random

def guess_game():
    number = random.randint(1, 100)
    guess = None

    print("Guess the number between 1 and 100!")

    while guess != number:
        guess = int(input("Enter your guess: "))

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("🎉 Correct! The number was", number)

guess_game()
