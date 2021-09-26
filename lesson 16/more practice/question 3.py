strings = [input("Enter a string: ") for i in range(5)]
strings.sort()
for string in strings:
  if string.startswith("x") or string.startswith("X"):
    strings.insert(0, strings.pop(strings.index(string)))
sorted_strings = [string for string in strings if string.startswith('x') or string.startswith("X")]
sorted_strings.sort()
strings = [string for string in strings if not string.startswith('x') or string.startswith("X")]
sorted_strings.extend(strings)
print(sorted_strings)
