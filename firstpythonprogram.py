#!/usr/bin/env python

import random

def main():
    print ("Guess a number between 1 and 100.")
    randomNumber = random.randint(1,100)
    found = False

    while not found:
        userGuess = input("Your guess: ")
        if int(userGuess) == randomNumber:
            print ("You got it!")
        elif int(userGuess) > randomNumber:
            print ("Guess lower!")
        else:
            print ("Guess higher!")



if __name__=="__main__":
    main()
