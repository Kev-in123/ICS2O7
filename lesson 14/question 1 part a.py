total = 0

word = input("Enter a word. Type \"quit\" to quit: ").lower()
while word != "quit":
  vowel = [i for i in range(len(word)) if "aeiou".find(word[i])!=-1]
  total += 1
  word = input("Enter a word. Type quit to quit: ").lower()
  
try:
  print(len(vowel)/total)
except ZeroDivisionError:
  print("Not enough words entered")

