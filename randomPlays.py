import random

randomNumber = random.randint(1, 10)
randomNumber = str(randomNumber)

print('Welcome to the guessing game!')
username = input('Enter username: ')

guessesTaken = 0

print(username, 'let the games begin!')

while guessesTaken < 6:
    guess = input('Guess number')
    guess = str(guess)

    guessesTaken += 1

    if guess < randomNumber:
        print("Go higher..")

    elif guess > randomNumber:
        print("Go lower..")

    elif guess == randomNumber:
        print("Congratulations")
        break

    else:
        print('Ran outta tries. The number was ', randomNumber)
        break

print('Random: ', randomNumber, '\nGuess: ', guess, '\nAttempts: ', guessesTaken)
