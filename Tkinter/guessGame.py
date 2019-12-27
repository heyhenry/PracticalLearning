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

window = Tk()
window.title('Welcome to the Games4Fun.')
window.geometry('500x500')

menu = Menu(window)

def randomNumbers():

    window.withdraw()
    global ng
    ng = Tk()
    ng.title("Numbers Game")
    ng.geometry('500x500')
    questionBox = Entry(ng, width=10)
    questionBox.pack()
    submit = Button(ng, text="Submit", command=randomNumbers)
    submit.pack()

    randomNo = random.randint(1, 10)

    intro = Label(ng, text="Welcome to the Numbers game.")
    intro.pack()
    question = Label(ng, text="Guess a number between 1 - 10.")
    question.pack()

    guess = int(questionBox.get())

    if guess == randomNo:
        messagebox.showinfo("Numbers Game", "You guessed correctly!")
        return False

    elif guess > randomNo:
        messagebox.showinfo("Numbers Game", "Lower...")
        return True

    elif guess < randomNo:
        messagebox.showinfo("Numbers Game", "Higher...")
        return True


game_item = Menu(menu, tearoff=0)
game_item.add_command(label='Random Number', command=randomNumbers)

menu.add_cascade(labe='Int Games', menu=game_item)
window.config(menu=menu)

window.mainloop()



