def y(m, x, b):
  y = m*x+b
  return y

while True:
  slope = float(input("Enter the slope: "))
  y_int = float(input("Enter the y-int: "))
  try:
    x_value = float(input("Enter an x-value (enter a string to exit): "))
  except ValueError:
    break
  print(f"The y value is {y(slope, x_value, y_int)}")
print("End of program")