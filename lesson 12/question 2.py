words = [len(str(input("Enter a word: "))) for i in range(10)]
print(f"The average length is {sum(words)/len(words)}")