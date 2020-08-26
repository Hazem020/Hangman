import random

print('H A N G M A N')
words = ('python', 'java', 'kotlin', 'javascript')
word = random.choice(words)
guessed = input('Guess the word:')
if guessed == word:
    print('You survived!')
else:
    print('You are hanged!')