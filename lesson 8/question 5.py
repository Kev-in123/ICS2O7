occasions = {
  "Christmas":"Merry Christmas!",
  "Birthday":"Happy Birthday!",
  "New Years":"Happy New Year!",
}

while True:

  occasion = str(input(f"Hi!\nWhat occasion is it? Here are the ones I know:\n{list(occasions.keys())}\n"))

 
  try:
    occasion = occasion.title()
    print(occasions[occasion])
    
  except KeyError:
    print("I do not know of such occasion.")
    break

print("End of program")
