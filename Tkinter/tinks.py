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

# # Combo Box widget
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

# # Check button widget
# from tkinter import *
# from tkinter.ttk import *
#
# window = Tk()
# window.title("Welcome to Tinks4Fun app")
# window.geometry('450x300')
# chk_state = BooleanVar()
# # Can also use an alternative
# # chk_state = IntVar()
# # chk_state.set(0) # True
# # chk_state.set(1) # False
# chk_state.set(True) # set check state
# chk = Checkbutton(window, text='Choose', var=chk_state)
# chk.grid(column=0, row=0)
# window.mainloop()

# # Radio button widget
# from tkinter import *
# from tkinter.ttk import *
#
# window = Tk()
# window.title("Welcome to Tinks4Fun")
# window.geometry('450x300')
# lbl = Label(window, text="Radio button:")
# lbl.grid(column=0, row=0)
# selected = IntVar()
# rad1 = Radiobutton(window, text='First', value=1, variable=selected)
# rad2 = Radiobutton(window, text='Second', value=2, variable=selected)
# rad3 = Radiobutton(window, text='Third', value=3, variable=selected)
#
# def clicked():
#     # Prints the value of the button chosen
#     print(selected.get())
# btn = Button(window, text="Click Me", command=clicked)
# rad1.grid(column=1, row=0)
# rad2.grid(column=2, row=0)
# rad3.grid(column=3, row=0)
# btn.grid(column=4, row=0)
# window.mainloop()

# # ScrolledText widget
# from tkinter import *
# from tkinter import scrolledtext
#
# window = Tk()
# window.title("Welcome to Tinks4Fun app")
# window.geometry('450x300')
#
# txt = scrolledtext.ScrolledText(window, width=40, height=10)
# txt.grid(column=0, row=0)
# txt.insert(INSERT, "Your text goes here ")
# # To clear the contents of a ScrolledText widget
# # txt.delete(1.0, END)
#
# window.mainloop()

# # Message Box Widget
# from tkinter import *
# from tkinter import messagebox
#
# window = Tk()
# window.title("Welcome to Tinks4Fun app")
# window.geometry('450x300')
#
# def clicked():
#     messagebox.showinfo("This is the message box title", "Hey, this is the content of the message box!")
#
# btn = Button(window, text="Click here", command=clicked)
# btn.grid(column=0, row=0)
#
# window.mainloop()