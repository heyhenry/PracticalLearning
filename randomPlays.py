import random

randomNumber = random.randint(1, 10)
randomNumber = str(randomNumber)

print('✯ Welcome to the guessing game ✯')
username = input('✯ Enter username: ')

guessesTaken = 0

print(username, 'is it? \nGreat name! \nOkay, the rules are simple.\n')
print('⚘ You have 6 attempts. \n⚘ Enter a number ranging between 1 - 10. \n⚘ Heed the warnings after each attempt.\n')

while guessesTaken < 6:
    guess = input('Guess the number:')
    guess = str(guess)

    guessesTaken += 1

    if guess < randomNumber:
        print("A little higher...")

    elif guess > randomNumber:
        print("A little lower...")

    elif guess == randomNumber:
        print("\nCongratulations! You guessed it right!")
        break

if guess != randomNumber:
    print('\nOh no! You ran out of attempts. The correct number was', randomNumber + '.\n')

print('Taking you to the stats screen now...\n')
print('\nStats: ')
print('The actual number: ', randomNumber, '\nLast guess: ', guess, '\nAttempts taken: ', guessesTaken)
print('\nThank you. Come again ( ͡👁️ ͜ʖ ͡👁️)✊!')
