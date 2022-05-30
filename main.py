import random

#funcs
#utility
#region
def imgConvert(string):
    li = list(string.split('\n\n'))
    return li

def convert(string, breaker):
    li = list(string.split(breaker))
    return li
#endregion

# part of the program
def printGame(word, letters, image):
    print('\n' + image, 'Guessed letters:', str(letters))
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
f = open('library.txt', 'r')
myLib = convert(f.read(),'\n')  #convert to list, breaking at each newline
f.close()

#pick a random word from the list
word = myLib[random.randint(0, len(myLib))]

#guessed letters
letters = []
#wrong attempts for letters
wrong = 0

#run
f = open('image.txt', 'r')
myImages = imgConvert(f.read())
f.close()



while True:
    #print the game out, set win = True if all letters are guessed
    win = printGame(word, letters, myImages[wrong])

    guess = input("guess a letter\n> ")
    # increase 'wrong counter' if they make a wrong guess
    if guess not in list(word):
        wrong += 1
    
    #add the guess to the list of guesses
    letters.append(guess)
    
    # Lose if you guess wrong too many times
    if wrong >= len(myImages):
        print("You lose!\nThe word was: " + word)
        break
    
    #win condition
    if win:
        print("Congrats! You Won!")
        break

input()