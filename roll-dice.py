import random


# def game():
#     guessedCharacter = input("Roll the dice? (y/n): ")
#     if guessedCharacter.lower() == "n":
#         print("Thanks for playing")

#     elif guessedCharacter == "y":
#         print((random.randrange(1, 7), random.randrange(1, 7)))
#         game()

#     elif guessedCharacter != 'n' and guessedCharacter != 'y':
#         print("Invalid choice!")
#         game()


# game()

# solving by loop

while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1}, {die2})")
    elif choice == 'n':
        print("Thanks for playing")
        break
    else:
        print("Invalid choice!")
