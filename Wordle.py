import random
import sys

def main():
    
    answer = getRandomWord()
    attempts = 0
    guess = ''
    while attempts < 6 and guess != answer:
        guess = input('Enter a 5 letter guess?\n')
        attempts += 1
        printGuessColors(guess,answer)

    if attempts >= 6:
        print('You lost. The answer was ' + answer + '.')
    else:
        print('You Won! That took ' + str(attempts) + ' guess(es).')

    

def printGuessColors(guess, answer):
    for i in range(0,5):
        color = letterColor(i, guess, answer)
        print(guess[i] + ' - ' + color)
    return printGuessColors



def letterColor(i, guess, answer):
    letter = guess[i]
    if letter == answer[i]:
        return 'Green'
    elif letter not in answer:
        return 'Red'
    else:
        return 'Yellow'



def getRandomWord():

    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        file = open("words.txt", "r")
        words = [word.strip() for word in file.readlines()]

        return random.choice(words)


main()
