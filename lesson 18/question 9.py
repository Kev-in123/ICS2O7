longer = lambda words: max(words,key=len)

words = [input("Enter a word: ") for i in range(10)]
print(longer(words))
