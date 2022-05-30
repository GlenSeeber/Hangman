import random

#funcs
def printGame(word, letters, image):
    print('\n' + image)
    #blanks
    for i in word:
        # if the current letter is in 'letters', then print it
        if i in letters:
            print(i, end=' ')
        # otherwise, print a blank (the player hasn't guessed the letter yet)
        else:
            print('_', end=' ')
    #newline
    print('\n')

#run
image = (("x0" * 10) + "\n\n")
word = "orange"
letters = ['g', 'j', 'o']

printGame(word, letters, image)