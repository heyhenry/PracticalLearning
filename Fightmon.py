"""

=-=[ Fightmon ]=-=

A pokemon style / inspired turned based game
A practical means of learning the basics of python

"""

import random

startGame = True

playerHealth = 100
opponentHealth = 100

while startGame:
    print("*** || Fightmon || ***")
    playerName = input("Enter player name: ")
    print("Are you ready to fight a pokemon " + playerName + "?")
    ready = input("[yes] / [no]")

    if ready == 'yes':

        print("\nGreat! Let's go to the arena.")
        print("Dunidunidunidunidunidunidunnn")
        print("Okay, we're here.")
        readyLoop = True
        while readyLoop:
            print("You see that beast over in the ruby ring?")
            ans = input("[yes] / [no]")
            if ans == 'yes':
                print("\nAha, he's your opponent. Goes by the name Gorillakong.")
                print("Oh by the way, name's Syska. I'm your eternal guide and bookworm!")
                print("Now that that's out of the way, let me teleport you into the ring. Good luck!")
                print("Teleporting....\n")
                print("BATTLE START\n")

                coinLoop = True
                while coinLoop:
                    print("Choose heads or tails to see who attack first.")
                    coinflipList = ['heads', 'tails']
                    coinChoice = input("[heads] / [tails]\n")

                    # if user input does not match coinflipList, it will return to the beginning of while loop (coinLoop)
                    if coinChoice not in coinflipList:
                        print("Invalid response. Choose either heads or tails!\n")
                        continue

                    # if user input does match coinflipList, it will continue with statements
                    elif coinChoice in coinflipList:
                        print("The coin is flipped.")
                        # list holding heads and tails options
                        coinflip = random.choice(coinflipList)
                        print("The coin landed on " + coinflip + ".")

                        if coinflip == coinChoice:
                            print("You are starting.")
                            print("You are starting with " + str(playerHealth) + " health.")
                            break
                        elif coinflip != coinChoice:
                            print("Gorillakong is starting.")
                            print("Gorillakong has a starting health of " + str(opponentHealth))
                            break
                        else:
                            print("Invalid response! System shutdown initiated.")
                            print("Boom, crash, dead.")
                            break  # stops the game

            # takes them back to the start of the while statement
            elif ans == 'no':
                print("Oh.. then I think you'd best try again when you're at 100%\n")

            #  responses other than yes or no will promptly end game
            else:
                print("Sorry, I don't understand. Can you just answer with a yes or no?\n")
                continue

    #  loops back to the start of the while statement
    elif ready == 'no':
        print("Taking you back to the main screen.")
        print(". . . . .")
        print(". . . . \n")

    else:
        print("Invalid response! System shutdown initiated.")
        print("Boom, crash, dead.")
        break



