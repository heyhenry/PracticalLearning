import random


playerHealth = 100
opponentHealth = 100

playerSkills = {
    1: "Punch",
    2: "Heavy Swing",
    3: "Roundhouse Kick",
    4: "Guard"
}

opponentSkills = ['Smash', 'Roar', 'Punch', 'Slap']

coinFlipChoice = ['Heads', 'Tails']

username = input("Enter username: ")
print("Welcome to a fight " + username + ' .')
print("Your opponent is Gorillakong.\n")

print("*Battle Start*")

fight = True
while fight:
    print("Read to fight?")
    ans = input("Yes or no.")
    if ans == 'yes':
        coinFlip = True

        while coinFlip:
            print("\nChoose heads or tails to determine who starts")
            coinChoice = input("[Heads] / [Tails]")

            if coinChoice not in coinFlipChoice:
                print("Invalid response. Heads or Tails? \n")
                continue

            elif coinChoice in coinFlipChoice:
                print("\nCoin is flipped.")

                coinFlip = random.choice(coinFlipChoice)
                print("The coin landed on "+ coinFlip + ".")

                if coinFlip == coinChoice:
                    print("\nYou are starting.")

                if coinFlip != coinChoice:
                    print("\nGorillakong is starting.")

            print(username + " is starting at " + str(playerHealth) + " healthpoints.\nGorillakong is starting at " + str(opponentHealth) + " healthpoints." )
    else:
        print("Systems shutting down..")
        break


# def playerSkills()
#     print("[1] Jab | [2] Heavy Swing | [3] Roundhouse Kick | [4] Guard Up")
