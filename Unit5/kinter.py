from tkinter import *
import tkinter


def hello():
    print("hello")


def goodbye():
    print("goodbye")


root = tkinter.Tk()
root.geometry("300x300")
menubutton = Menubutton(root, text="this is here")
menubutton.menu = Menu(menubutton)
menubutton["menu"] = menubutton.menu
menubutton.menu.add_command(label="op1", command=hello)
menubutton.menu.add_command(label="op2", command=goodbye)
menubutton.pack()
root.mainloop()
