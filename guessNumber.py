# Guess the number game

import random

# variable that generates random number
randomNum = random.randint(1, 10)

# attempts taken variable
guessesTaken = 0

# loop til 6 guesses are given or guessed correctly before then
while guessesTaken < 6:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    # indicators on closeness of the guesses
    if guess < randomNum:
        print("Too Low")
    elif guess > randomNum:
        print("Too High")

    # validation of correct guess, leading to end of game and success message
    elif guess == randomNum:
        print("You guessed correctly!" + " Guess was: " + str(guess) + " Random number was: " + str(randomNum))
        break

# validation after attempts are used and failure beckons with message, ending game
if guess != randomNum:
    print("You ran out of guesses." + " It was: " + str(randomNum))