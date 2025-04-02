# Given a string input, shorten the word to initial character, the number of letters minus the first
# and last character, and last character.

# EG:
# accessibility -> a11y
# Test this -> t3t t2s

def shorten_word(word=None):
    if word == None:
        return ""
    
    words = word.split()
    results = []

    for i in words:
        i = i.lower()
        if len(i) < 3:
            results.append(i)
        else:
            results.append(i[0] + str(len(i) -2) + i[-1])
    
    return ' '.join(results)

print(shorten_word("accessibility")) # a11y
print(shorten_word("Test this")) # t3t t2s
print(shorten_word("")) # ""
print(shorten_word(None)) # ""