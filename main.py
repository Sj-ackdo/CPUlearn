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
    if entries[num].config == 0:
        entries[num].text == 1
    else: entries[num].text = 0











# GUI stuff
importButton = Button(root, text="File import", bg=bgColor, justify="center")
importButton.grid(row=0, column=0)

inputLabel = Label(root, text="Instruction", bg=bgColor, justify="center")
inputLabel.grid(row=1, column=0)

inputrow = 1
inputcollumn = 1
entrytext = StringVar(root)
entrytext.set(0)

entries = [
    Button(root, command=lambda:switch(0), width=2, textvariable=entrytext, justify="center"),
    Button(root, command=lambda:switch(1), width=2, textvariable=entrytext, justify="center"),
    Button(root, command=lambda:switch(2), width=2, textvariable=entrytext, justify="center"),
    Button(root, command=lambda:switch(3), width=2, textvariable=entrytext, justify="center"),
    Button(root, command=lambda:switch(4), width=2, textvariable=entrytext, justify="center"),
    Button(root, command=lambda:switch(5), width=2, textvariable=entrytext, justify="center"),
    Button(root, command=lambda:switch(6), width=2, textvariable=entrytext, justify="center"),
    Button(root, command=lambda:switch(7), width=2, textvariable=entrytext, justify="center")
]

for i in range(0, 8):
    entries[i].grid(row=inputrow, column=(inputcollumn+i))

# Hou onderaan
root.mainloop()