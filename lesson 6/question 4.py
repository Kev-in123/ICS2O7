PST = 0.07
GST = 0.06

price = float(input("what is the price of the item: "))
taxable = input("is this item taxable? ")

if taxable == "yes":
  pst = PST * price
  gst = GST * price
  print(f"the price is {price}")
  print(f"the pst of this item is {pst:.2f}")
  print(f"the gst of this item is {gst:.2f}")
  print(f"the total cost of this item is $ {price + pst + gst}")

else:
  print(f"the price is  {price}")
