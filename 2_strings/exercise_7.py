def translate(letter):
    vowels = 'aeiou'
    if letter in vowels:
        return 'ub' + letter
    return letter

def ubbi_dubbi(word):
    return ''.join(map(translate, word))

print(ubbi_dubbi('elephant'))