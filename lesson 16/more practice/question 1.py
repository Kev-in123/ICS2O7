names = [input("Enter a name: ") for i in range(5)]
print("----------------------------")
for name in names:
  if name.startswith("P"):
    print(name)
print("----------------------------")

start = input("Enter a starting letter: ")
for name in names:
  if name.startswith(start.upper()):
    print(name)
print("----------------------------")

for i in range(len(names)):
  for j in range(len(names[i])):
    if names[i][j].isdigit():
      print(names[i])
