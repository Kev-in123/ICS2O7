word = input("Enter a word.").lower()

new_word = [word[i].upper() if word[i].isalpha and "aeiou".find(word[i]) != -1 else word[i].lower() for i in range(len(word))]
        
print(''.join(new_word))










