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
# # # Different types of message boxes
# # messagebox.showwarning('Message title', 'Show Warning')
# # messagebox.showerror('Message title', 'Show Error')
# # messagebox.showinfo('Message title', 'Show Info')
# # res = messagebox.askquestion('Message title', 'Ask Question')
# # res = messagebox.askyesno('Message title', 'Ask Yes No')
# # res = messagebox.askyesnocancel('Message title', 'Ask Yes No Cancel')
# # res = messagebox.askokcancel('Message title', 'Ask Ok Cancel')
# # res = messagebox.askretrycancel('Message title', 'Ask Retry Cancel')
#
#
# def clicked():
#     messagebox.showinfo("This is the message box title", "Hey, this is the content of the message box!")
#
# btn = Button(window, text="Click here", command=clicked)
# btn.grid(column=0, row=0)
#
# window.mainloop()


# # Spin Box Widget
# from tkinter import *
#
# window = Tk()
# window.title("Welcome to Tinks4Fun")
# window.geometry('450x300')
#
# spin = Spinbox(window, from_=0, to=100)
# # # Specify numbers in Spinbox
# # spin = Spinbox(window, values=(3, 8, 11), width=5)
#
# # # Set a default value for Spinbox and pass said value through textvariable parameter
# # var = IntVar()
# # var.set(36)
# # spin = Spinbox(window, from_=0, to=40, width=5, textvariable=var)
#
# spin.grid(column=0, row=0)
# window.mainloop()


# # Progress Bar Widget
# from tkinter import *
# from tkinter.ttk import Progressbar
# from tkinter import ttk
#
# window = Tk()
# window.title("Welcome to Tinks4Fun")
# window.geometry('450x300')
# style = ttk.Style()
# style.theme_use('default')
# style.configure("green.Horizontal.TProgressbar", background='green')
# bar = Progressbar(window, length=200, style="green.Horizontal.TProgressbar")
# bar['value'] = 70
# bar.grid(column=0, row=0)
# window.mainloop()


# # File Dialog Widget
# from tkinter import filedialog
#
# file = filedialog.askopenfilename()
#
# # # For multiple files
# # files = filedialog.askopenfilenames()
#
# # # For specific tile types
# # file = filedialog.askopenfilename(filetypes = (("Text files", "*.txt"), ("all files", "*.*")))
#
# # # For directory
# # dir = filedialog.askdirectory()
#
# # # For specific initial directory
# # from os import path
# # file = filedialog.askopenfilename(initialdir= path.dirname(__file__))


# # Menu Bar Widget
# from tkinter import *
# from tkinter import Menu
# from tkinter import messagebox
#
# window = Tk()
# window.title('Welcome to Tink4Fun app')
# menu = Menu(window)
# new_item = Menu(menu)
# second_item = Menu(menu, tearoff=0)
#
# menu.add_cascade(label='File', menu=new_item)
# menu.add_cascade(label='Git', menu=second_item)
#
#
# def clicked():
#     messagebox.showinfo('Push', 'You have successfully pushed your python file.')
#
# new_item.add_command(label='New')
# new_item.add_separator()
# new_item.add_command(label='Edit')
# new_item.add_separator()
#
# second_item.add_separator()
# second_item.add_command(label='Push', command=clicked)
# second_item.add_separator()
# second_item.add_command(label='Pull')
# second_item.add_separator()
# second_item.add_command(label='Commit')
# second_item.add_separator()
#
# window.config(menu=menu)
#
# window.mainloop()


# # Notebook Widget
# from tkinter import *
# from tkinter import ttk
#
# window = Tk()
# window.title('Welcome to Tinks4Fun app')
#
# tab_control = ttk.Notebook(window)
#
# tab1 = ttk.Frame(tab_control)
# tab2 = ttk.Frame(tab_control)
# tab_control.add(tab1, text='First')
# tab_control.add(tab2, text='Second')
#
# lbl1 = Label(tab1, text='Label 1', padx=5, pady=5)
# lbl1.grid(column=0, row=0)
# lbl2 = Label(tab2, text='Label 2')
# lbl2.grid(column=0, row=0)
#
# tab_control.pack(expand=1, fill='both')

# window.mainloop()