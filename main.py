import random

from numpy import true_divide

#funcs
#utility
#region
def convert(string):
    li = list(string.split('\n\n'))
    return li
#endregion

# part of the program
def printGame(word, letters, image):
    print('\n' + image)
    win = True
    #blanks
    for i in word:
        # if the current letter is in 'letters', then print it
        if i in letters:
            print(i, end=' ')
        # otherwise, print a blank (the player hasn't guessed the letter yet)
        else:
            print('_', end=' ')
            win = False
    #newline
    print('\n')
    # returns true if you won the game
    return win

#vars

#the word must guess
word = "orange"
#guessed letters
letters = []
#wrong attempts for letters
wrong = 0

#run
f = open('image.txt', 'r')
myImages = convert(f.read())
f.close()

while True:
    guess = input("guess a letter\n> ")
    # increase 'wrong counter' if they make a wrong guess
    if guess not in list(word):
        wrong += 1
    #add the guess to the list of guesses
    letters.append(guess)
    # Lose if you guess wrong too many times
    if wrong >= len(myImages):
        print("You lose!")
        break
    #print the game out, set win = True if all letters are guessed
    win = printGame(word, letters, myImages[wrong])
    #win condition
    if win:
        print("Congrats! You Won!")
        break

input()