from tkinter import *
from tkinter import Menu
from tkinter import messagebox

window = Tk()
window.title("Welcome to add game.")
window.geometry('350x450')

menu = Menu(window)



def Addition():

    window.withdraw()
    global addGame
    addGame = Tk()
    window.title("Addition Game")
    addGame.geometry('500x500')
    intro = Label(addGame, text="Let's add two numbers together.", font=("Lucida Console", 10))
    intro.grid(column=0, row=0)

    firstNo = Label(addGame, text="First Number:", font=("Lucida Console", 10))
    firstNo.grid(column=0, row=1)
    txt1 = Entry(addGame, width=10)
    txt1.grid(column=0, row=2)

    secondNo = Label(addGame, text="Second Number:", font=("Lucida Console", 10))
    secondNo.grid(column=1, row=1)
    txt2 = Entry(addGame, width=10)
    txt2.grid(column=1, row=2)

    def ans():

        firstNum = txt1.get()
        secondNum = txt2.get()

        firstNum = int(firstNum)
        secondNum = int(secondNum)

        ans = firstNum + secondNum
        messagebox.showinfo('Solution', "The answer is: " + str(ans) + '.')

    btn = Button(addGame, text='Enter', command=ans)
    btn.grid(column=0, row=3)


game_item = Menu(menu, tearoff=0)
game_item.add_command(label="Addition", command=Addition)

menu.add_cascade(label="Math Games", menu=game_item)
window.config(menu=menu)


window.mainloop()