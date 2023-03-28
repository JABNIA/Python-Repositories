def is_vowel(word):
    word_short = ""
    for i in word:  
        if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or
        i == "A" or i == "E" or i == "I" or i == "O" or i == "U" ):
            continue
        else:
            word_short += i
        
    return word_short
    