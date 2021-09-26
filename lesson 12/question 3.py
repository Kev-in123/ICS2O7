words = []

word = str(input("Enter a word: "))

while len(word)!=0:
  words.append(len(word))
  word = str(input("Enter a word: "))


print(f"The average length is {sum(words)/len(words)}")