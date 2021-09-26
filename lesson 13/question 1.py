
word = input("Enter a word: ")

print(f"The word in exchanged case is: {word.swapcase()}")
print("----------------------------------")

alt_word = [word[i].upper() if not i % 2 else word[i].lower() for i in range(len(word))]
print(f"The word in alternating upper and lower case is: {''.join(alt_word)}")
print("----------------------------------")


alt_word_2 = [word[i].upper() if not i % 2 else word[i].lower() for i in range(len(word))]
print(f"The word in alternating lower and upper case is: {''.join(alt_word_2)}")
print("----------------------------------")


half = int(len(word)/2)
upFirst = word[:half].upper() + word[half:].lower()
print(f"The word with an upshifted first half is: {upFirst}")
print("----------------------------------")


upSecond = word[:half].lower() + word[half:].upper()
print(f"The word with an upshifted second half is: {upSecond}")
print("----------------------------------")
