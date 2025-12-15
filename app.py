import random


def game():
    guessedCharacter = input("Roll the dice? (y/n): ")
    if guessedCharacter.lower() == "n":
        print("Thanks for playing")

    elif guessedCharacter == "y":
        print((random.randrange(1, 7), random.randrange(1, 7)))
        game()

    elif guessedCharacter != 'n' and guessedCharacter != 'y':
        print("Invalid choice!")
        game()


game()
