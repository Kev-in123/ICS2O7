heights = []

height = float(input("Enter a height (0 or a negative number to exit): "))

while height > 0:
  if height <= 0:
    break
  heights.append(height)
  height = float(input("Enter a height (0 or a negative number to exit): "))

try:
  print(f"The average height is {(sum(heights)/len(heights)):.2f}")
except ZeroDivisionError:
  print("No average")
