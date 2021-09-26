street = input("what is your street adress? ")
city = input("what city do you live in? ")
country = input("what country do you live in? ")

if country.lower() == "canada":
  province = input("what province do you live in? ")
  postal = input("what is your postal code? ")
  print(f"Address: {street}")
  print(f"{city}, {province} {postal}")
  print(country)
    
elif country.lower() == "usa":
  state = input("what state do you live in?")
  zipcode = input("what is your zip code")
  print(f"Address: {street}")
  print(f"{city}, {state} {zipcode}")
  print(country)

else:
  print("you don't live in Canada or the US")
