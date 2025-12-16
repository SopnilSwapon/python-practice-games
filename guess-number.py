import random

guess_to_number = random.randint(1, 100)

while True:
    try:
       user_input_number = input("Your guess number?: ")
       if int(user_input_number) > guess_to_number:
          print("It's too High!")
       elif int(user_input_number) < guess_to_number:
          print("It's too low!")
       else:
          print("Congratulations, You guess it!!")
          break
    except ValueError:
        print("Please enter a valid number")
