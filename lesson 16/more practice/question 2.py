strings = [input("Enter a string: ") for i in range(5)]
for string in strings:
  if len(string) > 4:
    print(string)
  if string[0] == string[-1]:
    print(string)
