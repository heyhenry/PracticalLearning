import random

randomNo = random.randint(1, 10)

tries = 0
guess = 0

print("Welcome to the number's guessing game.")

while tries < 6:

    tries +=1

    guess = input("Guess a number between 1 and 10.")
    guess = int(guess)

    if guess < randomNo:
        print('Higher...')

    elif guess > randomNo:
        print('Lower...')

    elif guess == randomNo:
        break

if guess == randomNo:
    print("You guessed correctly! \nIt was indeed " + str(randomNo) + '.')

elif guess !=  randomNo:
    print("You ran out of guesses. \nThe number was " + str(randomNo) + '.')

