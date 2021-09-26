word = input("Enter a word: ")

wordRemoveLower = ''.join(x for x in word if not x.islower())
print(wordRemoveLower)

wordRemoveUpper = ''.join(x for x in word if not x.isupper())
print(wordRemoveUpper)
