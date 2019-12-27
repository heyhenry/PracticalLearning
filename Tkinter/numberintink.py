from tkinter import *
from tkinter import Menu

window = Tk()
window.title("Welcome to add game.")
window.geometry('350x450')

menu = Menu(window)



def Addition():

    addGame = Tk()
    window.title("Addition Game")
    addGame.geometry('350x450')
    intro = Label(addGame, text="Let's add two numbers together.")
    intro.grid(column=0, row=0)

game_item = Menu(menu)
game_item.add_command(label="Addition", command=Addition)

menu.add_cascade(label="Math Games", menu=game_item)
window.config(menu=menu)

window.mainloop()