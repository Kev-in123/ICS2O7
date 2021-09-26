juliaAmt = 300.0
maxAmt = 280.0
year = 0

while maxAmt < juliaAmt:
  year += 1
  juliaAmt *= 1.0125
  maxAmt *= 1.02
  print(f"At the end of year number {year}\nJuilas' balance: {juliaAmt}\nMaxs' balance: {maxAmt}")
  print(f"----- End of year {year} -----")

print(f"It will take {year} years for Max to overtake Julia")
