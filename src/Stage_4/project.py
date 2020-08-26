import random


print('H A N G M A N')
words = ('python', 'java', 'kotlin', 'javascript')
word = random.choice(words)
guessed = input(f'Guess the word {word[:3] + "-" * (len(word) - 3)}:')
if guessed == word:
    print('You survived!')
else:
    print('You are hanged!')
