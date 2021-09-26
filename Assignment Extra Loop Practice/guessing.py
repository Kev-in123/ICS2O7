programmer_num = int(input("Enter a number for the user to guess: "))

num = int(input("Enter a number: "))

while num != programmer_num:

  if num > programmer_num:

      num = int(input("Incorrect please try again (hint: your number was too high): "))

  elif num < programmer_num:

      num = int(input("Incorrect please try again (hint: your number was too low): "))

print("You got the right number")
