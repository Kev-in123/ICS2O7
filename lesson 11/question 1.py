import random
for i in range(5):
  num = random.randint(2, 10)
  word = input(f"Please enter a word that is {num} letters long: ")

  if len(word) != num:
    print("Word is not long enough/too long")
  if len(word) != num:
    print(f"{word} is not {num} letters long")
