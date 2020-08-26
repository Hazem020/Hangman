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
win = False
while attempts < 8:
    print('\n' + encrypted)
    if word == encrypted:
        win = True
    letter = input('Input a letter:')
    if letter not in word:
        print('No such letter in the word')
        attempts += 1
    elif letter in encrypted:
        print('No improvements')
        attempts += 1
    else:
        encrypted = replace(letter, encrypted)

if win:
    print('You survived!')
else:
    print('You are hanged!')