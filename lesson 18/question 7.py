def to_star(word):
  vowels = ['a', 'e' ,'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  for char in vowels:
    word = word.replace(char,"*")
  return word

word = input("Enter a word: ")
print(to_star(word))