def number():
  while True:
    try:
      num1 = int(input("Enter a number: "))
      num2 = int(input("Enter a number: "))
      break
    except ValueError:
      print("One of the values entered is not an integer, try again")

  while num1 < 1 or num2 < 1:
    print("One of the numbers isnt a positive integer try again")
    try:
      num1 = int(input("Enter a number: "))
      num2 = int(input("Enter a number: "))
      break
    except ValueError:
      print("One of the values entered is not an integer, try again")

  print(f"The larger number is: {max(num1,num2)}")
  again = input("Would you like to go again? ")
  if again.lower == "yes":
    number()
  elif again.lower() == "no":
    pass
  else:
    print("Invalid")
  
number()
