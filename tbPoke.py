"""

=-=[ Fightmon ]=-=

A pokemon style / inspired turned based game
A practical means of learning the basics of python

"""

import random

startGame = True

while startGame:
    print("*** || Fightmon || ***")
    playerName = input("Enter player name: ")
    print("Are you ready to fight a pokemon " + playerName + "?")
    ready = input("[yes] / [no]")
    if ready == 'yes':
        print("Great! Let's go to the arena.")
        print("Dunidunidunidunidunidunidunnn")
        print("Okay, we're here. You see that fella over there?")
        ans = input("[yes] / [no]")
        if ans == 'yes':
            print("Aha, he's your opponent. Goes by the name Gorillakong.")
        elif ans =='no':
            print("Okay.. well, he's your opponent, Gorillakong.")


        else:
            print("Invalid response! System shutdown initiated.")
            print("Boom.")
            break # stops the app

    # loops back to the start of the while statement
    elif ready == 'no':
        print("Taking you back to the main screen")
        print(". . . . .")
        print(". . . .")
        print(". . .")

    else:
        print("Invalid response! System shutdown initiated.")
        print("Boom.")
        break



