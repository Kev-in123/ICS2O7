magic_number = 3

# Your code here...
while True:
    user_guess = int(input("Please guess a number between 1 and 100: "))
    if user_guess == magic_number:
        print("Correct!")
        break
    elif user_guess < magic_number:
        print("Too low")
    else:
        print("Too high")