word = input("Enter a word: ").lower()

new_word = ["9" if word[i].isalpha and "aeiou".find(word[i]) == -1 else word[i] for i in range(len(word))]

print(''.join(new_word))

