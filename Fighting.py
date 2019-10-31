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

coinFlipChoice = ['heads', 'tails']

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
            coinChoice = input("[Heads] / [Tails]").lower()

            if coinChoice not in coinFlipChoice:
                print("Invalid response. Heads or Tails? \n")
                continue

            elif coinChoice in coinFlipChoice:
                print("\nCoin is flipped.")

                coinFlip = random.choice(coinFlipChoice)
                print("The coin landed on "+ coinFlip + ".")

                if coinFlip == coinChoice:
                    print("\nYou are starting.")

                elif coinFlip != coinChoice:
                    print("\nGorillakong is starting.")

            print(username + " is starting at " + str(playerHealth) + " healthpoints.\nGorillakong is starting at " + str(opponentHealth) + " healthpoints.\n" )

            if coinFlip != coinChoice:
                print("Gorillakong used " + random.choice(opponentSkills) + ".")

                if random.choice(opponentSkills) == 'Smash':
                    playerHealth -= 60
                    print(username + " is at" + str(playerHealth) + ".")
                    print("Gorillakong is at" + str(opponentHealth) + ".")

                elif random.choice(opponentSkills) == 'Roar':
                    playerHealth -= 20
                    print(username + " is at" + str(playerHealth) + ".")
                    print("Gorillakong is at" + str(opponentHealth) + ".")

                elif random.choice(opponentSkills) == 'Punch':
                    playerHealth -= 40
                    print(username + " is at" + str(playerHealth) + ".")
                    print("Gorillakong is at" + str(opponentHealth) + ".")

                elif random.choice(opponentSkills) == 'Slap':
                    playerHealth -= 30
                    print(username + " is at" + str(playerHealth) + ".")
                    print("Gorillakong is at" + str(opponentHealth) + ".")

            elif coinFlip == coinChoice:
                print(username + " used " + random.choice(playerSkills) + ".")

                if random.choice(playerSkills) == 'Jab':
                    opponentHealth -= 20
                    print(username + " is at" + str(playerHealth) + ".")
                    print("Gorillakong is at" + str(opponentHealth) + ".")

                elif random.choice(playerSkills) == 'Heavy Swing':
                    opponentHealth -= 50
                    print(username + " is at" + str(playerHealth) + ".")
                    print("Gorillakong is at" + str(opponentHealth) + ".")

                elif random.choice(playerSkills) == 'Roundhouse Kick':
                    opponentHealth -= 70
                    print(username + " is at" + str(playerHealth) + ".")
                    print("Gorillakong is at" + str(opponentHealth) + ".")

                elif random.choice(playerSkills) == 'Guard':
                    opponentHealth += 30
                    print(username + " is at" + str(playerHealth) + ".")
                    print("Gorillakong is at" + str(opponentHealth) + ".")
    else:
        print("Systems shutting down..")
        break


# def playerSkills()
#     print("[1] Jab | [2] Heavy Swing | [3] Roundhouse Kick | [4] Guard Up")
