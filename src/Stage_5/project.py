import random


def replace(let, enc):
    global word
    enc = list(enc)
    i = 0
    while i < len(word):
        if word[i] == let:
            enc[i] = let
        i += 1
    return ''.join(enc)


print('H A N G M A N')
words = ('python', 'java', 'kotlin', 'javascript')
word = random.choice(words)
encrypted = len(word) * '-'
attempts = 0
while attempts < 8:
    print('\n' + encrypted)
    letter = input('Input a letter:')
    if letter not in word:
        print('No such letter in the word')
    else:
        encrypted = replace(letter, encrypted)
    attempts += 1

print('\nThanks for playing!\n'
      'We\'ll see how well you did in the next stage')
