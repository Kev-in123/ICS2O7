# update the function to return `word` with all instances of `letter` removed!
def remove_all_from_string(word, letter):
    new_word=""
    for char in word:
        if char!=letter:
            new_word+=char
        else:
            pass
        
    return new_word