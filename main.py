# Imports
from tkinter import *
import os, sys
import struct

# Window
bgColor = "#C3C3C3"

# create input file
try:
    with open(os.path.join(sys.path[0], "input.bin"), "w") as ifile:
        pass
except PermissionError:
    print("Can't access file")


root = Tk()
root.geometry("400x400")
root.title("CPU")
root.resizable(False, False)
root.configure(bg=bgColor)
root.iconbitmap(os.path.join(sys.path[0], os.path.join("images", "Icon.ico")))

# Functions
def main():
    pass

def switch(num):

    if entries[num].config("text")[-1] == "0":
        entries[num].config(text = "1")
    else: entries[num].config(text = "0")

def create_window():
    top_window = Toplevel()
    e = Label(top_window, text="wah")
    e.pack









# GUI stuff
importButton = Button(root, command=create_window, text="File import", bg=bgColor, justify="center")
importButton.grid(row=0, column=0)

inputLabel = Label(root, text="Instruction", bg=bgColor, justify="center")
inputLabel.grid(row=1, column=0)

registerxLabel = Label(root, text="Register X:", bg=bgColor, justify="center")
registerxLabel.grid(row=2, column=0)
registerxvalueLabel = Label(root, text="NULL", bg=bgColor, justify="center")
registerxvalueLabel.grid(row=2, column=1)

registeryLabel = Label(root, text="Register Y:", bg=bgColor, justify="center")
registeryLabel.grid(row=2, column=2)
registeryvalueLabel = Label(root, text="NULL", bg=bgColor, justify="center")
registeryvalueLabel.grid(row=2, column=3)

# bit input buttons
framebuttons = Frame(root, bg=bgColor)
framebuttons.grid(row=1, column=1)

entries = [
    Button(framebuttons, command=lambda:switch(0), width=2, text="0", justify="center"),
    Button(framebuttons, command=lambda:switch(1), width=2, text="0", justify="center"),
    Button(framebuttons, command=lambda:switch(2), width=2, text="0", justify="center"),
    Button(framebuttons, command=lambda:switch(3), width=2, text="0", justify="center"),
    Button(framebuttons, command=lambda:switch(4), width=2, text="0", justify="center"),
    Button(framebuttons, command=lambda:switch(5), width=2, text="0", justify="center"),
    Button(framebuttons, command=lambda:switch(6), width=2, text="0", justify="center"),
    Button(framebuttons, command=lambda:switch(7), width=2, text="0", justify="center"),
]

# put bit input buttons on screen
for i in range(0, 8):
    entries[i].pack(side=RIGHT)

# Hou onderaan
root.mainloop()