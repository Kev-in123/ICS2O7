import random
ran_num = random.randint(0,100)
user_input = int(input("Guess my number (between 1 and 100 inclusive): "))

while user_input != ran_num:

  if user_input > ran_num:
    print("Too high! try again.")

  elif user_input < ran_num:
    print("Too low! try again. ")

  user_input = int(input("Guess my number (between 1 and 100 inclusive) "))

print("Correct!")
