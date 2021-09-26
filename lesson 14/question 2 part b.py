vowels=["a","e","i","o","u","A","E","I","O","U"]

word = input("Enter a word: ").lower()

for vowel in vowels:
  word = word.replace(vowel,"*")

print(word)
    