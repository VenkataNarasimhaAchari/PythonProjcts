from tkinter import *
from tkinter import ttk

root = Tk()


def show():
    print('The Button Was Clicked!')


button = ttk.Button(root, text='Click Here!', command=show)
button.pack(padx=100, pady=50)

root.mainloop()
