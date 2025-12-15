import random

guess_to_number = random.randint(1, 100)

while True:
    user_input_number = input("Your guess number?: ")
    if int(user_input_number) > guess_to_number:
        print("It's too High!")
    elif int(user_input_number) < guess_to_number:
        print("It's too low!")
    elif int(user_input_number) == guess_to_number:
        print("Congratulations, You guess it!!")
        break
    else:
        print("Provided wrong input")
