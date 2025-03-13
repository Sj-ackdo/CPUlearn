# Imports
from tkinter import *
import os, sys
import struct

# Window
bgColor = "#C3C3C3"

# create input file
# try:
#     with open(os.path.join(sys.path[0], "input.bin"), "w") as ifile:
#         pass
# except PermissionError:
#     print("Can't access file")


root = Tk()
root.geometry("400x400")
root.title("CPU")
root.resizable(False, False)
root.configure(bg=bgColor)
root.iconbitmap(os.path.join(sys.path[0], os.path.join("images", "Icon.ico")))

# Functions
def logic():
    create_window()

def step():
    outputLEDLabel.config(bg = "#00FF00")

def switch(num):

    if entries[num].config("text")[-1] == "0":
        entries[num].config(text = "1")
        entries[num].config(bg = "#00FF00")
    else: 
        entries[num].config(text = "0")
        entries[num].config(bg = "#FF0000")

def create_window():
    top_window = Toplevel()
    e = Label(top_window, text="wah")
    e.pack

def reset():
    # input bit buttons
    for i in range(0, 8):
        entries[i].config(text = "0")
        entries[i].config(bg = "#FF0000")

    # output led
    outputLEDLabel.config(bg = "#FF0000")






# GUI stuff
resetButton = Button(root, command=reset, width=5, text="Reset", bg=bgColor, justify="center")
resetButton.grid(row=0, column=0, columnspan=2, sticky="e", pady=(3,0))

stepButton = Button(root, command=step, width=5, text="Step", bg=bgColor, justify="center")
stepButton.grid(row=1, column=0, columnspan=2, sticky="e", pady=(3,0))

outputLabel = Label(root, text="Output:", bg=bgColor, justify="center")
outputLabel.grid(row=2, column=8, pady=(5,0))
outputLEDLabel = Label(root, width=2, bg="#FF0000", justify="center")
outputLEDLabel.grid(row=2, column=9, pady=(5,0))

logic1Button = Button(root, command=logic, width=5, text="Logic", bg=bgColor, justify="center")
logic1Button.grid(row=0, column=2, columnspan=2, sticky="e", pady=(3,0))

# registerxLabel = Label(root, text="Register X:", bg=bgColor, justify="center")
# registerxLabel.grid(row=2, column=0)
# registerxvalueLabel = Label(root, text="NULL", bg=bgColor, justify="center")
# registerxvalueLabel.grid(row=2, column=1)

# registeryLabel = Label(root, text="Register Y:", bg=bgColor, justify="center")
# registeryLabel.grid(row=2, column=2)
# registeryvalueLabel = Label(root, text="NULL", bg=bgColor, justify="center")
# registeryvalueLabel.grid(row=2, column=3)

# bit input buttons
# framebuttons = Frame(root, bg=bgColor)
# framebuttons.grid(row=1, column=1)

entries = [
    Button(root, command=lambda:switch(0), width=2, text="0", bg = "#FF0000", justify="center"),
    Button(root, command=lambda:switch(1), width=2, text="0", bg = "#FF0000", justify="center"),
    Button(root, command=lambda:switch(2), width=2, text="0", bg = "#FF0000", justify="center"),
    Button(root, command=lambda:switch(3), width=2, text="0", bg = "#FF0000", justify="center"),
    Button(root, command=lambda:switch(4), width=2, text="0", bg = "#FF0000", justify="center"),
    Button(root, command=lambda:switch(5), width=2, text="0", bg = "#FF0000", justify="center"),
    Button(root, command=lambda:switch(6), width=2, text="0", bg = "#FF0000", justify="center"),
    Button(root, command=lambda:switch(7), width=2, text="0", bg = "#FF0000", justify="center"),
]

# put bit input buttons on screen
for i in range(0, 8):
    entries[i].grid(row=2, column=i, pady=(5,0))

# Hou onderaan
root.mainloop()