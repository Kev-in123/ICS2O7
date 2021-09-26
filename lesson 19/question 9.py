def middle(word):
  index = len(word)//2
  if len(word) % 2 == 0: 
    return word[index-1]
  else:
    return word[index]

print(middle("Hi there"))