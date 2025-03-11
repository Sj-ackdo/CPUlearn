# Imports
from tkinter import *
import os, sys
import struct

# Window
bgColor = "#C3C3C3"

root = Tk()
root.geometry("400x400")
root.title("CPU")
root.resizable(False, False)
root.configure(bg=bgColor)
root.iconbitmap(os.path.join(sys.path[0], os.path.join("images", "Icon.ico")))

# Functions
def main():
    pass

# create input file
try:
    with open(os.path.join(sys.path[0], "input.bin"), "w") as ifile:
        pass
except PermissionError:
    print("Can't access file")

# GUI stuff
importButton = Button(root, text="File import", bg=bgColor, justify="center")
importButton.grid(row=0, column=0)

inputLabel = Label(root, text="Input", bg=bgColor, justify="center")
inputLabel.grid(row=1, column=0)

inputrow = 1
inputcollumn = 1

input1Entry = Button(root, width=2, justify="center")
input1Entry.grid(row=inputrow, column=inputcollumn)

input2Entry = Button(root, width=2, justify="center")
input2Entry.grid(row=inputrow, column=inputcollumn+1)

input3Entry = Button(root, width=2, justify="center")
input3Entry.grid(row=inputrow, column=inputcollumn+2)

input4Entry = Button(root, width=2, justify="center")
input4Entry.grid(row=inputrow, column=inputcollumn+3)

input5Entry = Button(root, width=2, justify="center")
input5Entry.grid(row=inputrow, column=inputcollumn+4)

input6Entry = Button(root, width=2, justify="center")
input6Entry.grid(row=inputrow, column=inputcollumn+5)

input7Entry = Button(root, width=2, justify="center")
input7Entry.grid(row=inputrow, column=inputcollumn+6)

input8Entry = Button(root, width=2, justify="center")
input8Entry.grid(row=inputrow, column=inputcollumn+7)

# Hou onderaan
root.mainloop()