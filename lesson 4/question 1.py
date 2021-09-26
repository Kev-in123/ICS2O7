import math
from math import pi

area = float(input("Enter an area"))
figure = input("Enter circle or square")

radius = (area/pi)**0.5


if figure.lower() == 'circle':
  circle = f"the radius is {radius} and the circumfrence is {pi*radius*2}"
  print(f"If the figure is a circle, {circle}")

length = area**0.5
width = length
perimeter = 4*length

if figure.lower() == 'square':
  square = f"the length and width are {length} and {width}, and the perimeter is {perimeter}"
  print(f"If the figure is a square, {square}")
