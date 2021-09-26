countryA = 50000000
countryB = 70000000
year = 0

while countryA < countryB:
  year += 1
  countryA *= 1.03
  countryB *= 1.02
  print(f"At the end of year number {year}\ncountry A population: {countryA}\ncountry B population: {countryB}")
  print(f"----- End of year {year} -----")

  print(f"It will take {year} years for country A to surpass country B\ncountry A population: {countryA:.0f}\ncountry B population: {countryB:.0f}")
  
