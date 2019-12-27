import random

# randomNo = random.randint(1, 10)
#
# tries = 0
# guess = 0
#
# print("Welcome to the number's guessing game.")
#
# while tries < 6:
#
#     tries +=1
#
#     guess = input("Guess a number between 1 and 10.")
#     guess = int(guess)
#
#     if guess < randomNo:
#         print('Higher...')
#
#     elif guess > randomNo:
#         print('Lower...')
#
#     elif guess == randomNo:
#         break
#
# if guess == randomNo:
#     print("You guessed correctly! \nIt was indeed " + str(randomNo) + '.')
#
# elif guess !=  randomNo:
#     print("You ran out of guesses. \nThe number was " + str(randomNo) + '.')

###################################

from tkinter import *
from tkinter import Menu
from tkinter import messagebox


def guessGame():
    guess = int(answer.get())
    print(guess)

    if guess < randomNo:
        messagebox.showinfo("Fun Games Inc", "Higher...")
        return True
    elif guess > randomNo:
        messagebox.showinfo("Fun Games Inc", "Lower...")
        return True
    elif guess == randomNo:
        messagebox.showinfo("Fun Games Inc", "You guessed correctly!")
        return False

window = Tk()
window.title("Fun Games Inc")
window.geometry('500x500')

question = Label(window, text="Choose a number between 1 - 10.")
question.pack()

answer = Entry(window, width=10)
answer.pack()

guess = Button(window, text="Submit", command=guessGame)
guess.pack()

randomNo = random.randint(1, 10)

window.mainloop()