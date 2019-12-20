# from tkinter import *
#
# window = Tk()
# window.title("Welcome to Tink4Fun app")
# window.geometry('450x200')
#
# lbl = Label(window, text='Hello', font=("Arial Black", 25))
# lbl.grid(column=0, row=0)
# # To disable entry widget, add 'state="disabled"' to the widget parameter
# txt = Entry(window, width=10)
# txt.grid(column=1, row=0)
# # Automatically focus into text box
# txt.focus()
#
#
# def clicked():
#     res = "Welcome to " + txt.get()
#     # Changes lbl's label message to the new message
#     lbl.configure(text=res)
#
#
# btn = Button(window, text="Click Me", command=clicked, bg="Light Blue", fg="Black")
# btn.grid(column=2, row=0)
#
# window.mainloop()

# # Combobox widget
# from tkinter import *
# from tkinter.ttk import *
#
# window = Tk()
# window.title("Welcome to Tinks4Fun app")
# window.geometry("450x300")
# lbl = Label(window, text="Select a number")
# lbl.grid(column=0, row=0)
# combo = Combobox(window)
# combo['values']= (1, 2, 3, 4, 5, "Text")
# combo.current(0) # Set the selected item
# combo.grid(column=1, row=0)
# window.mainloop()

# Check button widget
from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Welcome to Tinks4Fun app")
window.geometry('450x300')
chk_state = BooleanVar()
# Can also use an alternative
# chk_state = IntVar()
# chk_state.set(0) # True
# chk_state.set(1) # False
chk_state.set(True) # set check state
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=0, row=0)
window.mainloop()

