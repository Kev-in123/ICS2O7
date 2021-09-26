def remove_vowel(word):
  vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  for char in vowels:
    word = word.replace(char, "")
  return word


for i in range(5):
  word = input("Enter a word: ")
  print(remove_vowel(word))