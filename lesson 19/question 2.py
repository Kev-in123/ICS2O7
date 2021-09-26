def startsWithS(word):
  if word.lower().startswith("s"):
    return True
  else:
    return False

word = 'safety'
print(startsWithS(word))

word = 'laptop'
print(startsWithS(word))