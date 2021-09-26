while True:
  income = float(input("Income: "))
  if income <= 0:
    print("Invalid input")
    break

  elif 1 <= income <= 27500:
    tax = income*0.17
    print(f"tax: {tax}")

  elif income <= 55000:
    tax = 27500 * 0.17 + (40000-27500) * 0.24
    print(f"tax: {tax}")
  
  else:
    tax = 27500 * 0.17 + (40000-27500) * 0.24 + (income-55000) * 0.29
    print(f"tax: {tax}")


print("End of program")
