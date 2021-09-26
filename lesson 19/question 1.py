def integer():
  try:
    var = int(input("Enter an integer: "))
  except ValueError:
    var = "Invalid"
  return var

print(integer())