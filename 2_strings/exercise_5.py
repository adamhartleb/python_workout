def pig_latin(word):
    word = word.lower()
    vowels = 'aeiou'

    first_letter = word[0]
    if first_letter in vowels:
        return word + 'way'
    else:
        return word[1:] + word[0] + 'ay'

print(pig_latin('computer'))
print(pig_latin('air'))