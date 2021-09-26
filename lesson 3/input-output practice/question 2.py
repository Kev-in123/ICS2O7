p1 = 0
p2 = 0
dist = 0


coord1 = float(input("Enter coordinates of the first point: \n"))
coord2 = float(input())
coord3 = float(input("Enter coordinates of the second point: \n"))
coord4 = float(input())

p1 = abs(coord1-coord3) 
p2 = abs(coord2-coord4) 
dist = (p1**2+p2**2)
dist **= 0.5

print(f'The distance between ({coord1},{coord2}) and ({coord3},{coord4}) is {dist}')



