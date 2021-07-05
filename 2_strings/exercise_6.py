def pig_latin_word(word):
    word = word.lower()
    vowels = 'aeiou'

    first_letter = word[0]
    if first_letter in vowels:
        return word + 'way'
    else:
        return word[1:] + word[0] + 'ay'

def pig_latin_sentence(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    words = map(pig_latin_word, words)
    return " ".join(words)

print(pig_latin_sentence('this is a test translation'))
