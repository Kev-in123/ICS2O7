def remove_all_from_string(word1, word2):
    while word2 in word1:
        word1 = word1[:word1.find(word2)]+word1[word1.find(word2)+len(word2):]
    return word1

print(remove_all_from_string("bananas", "na"))