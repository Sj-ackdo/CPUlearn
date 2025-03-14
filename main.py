# Imports
from tkinter import *
import os, sys
# from MC14500 import Yin

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
    create_top_window()

def step():
    outputLEDLabel.config(bg = "#00FF00")

def switch(num):

    if num < len(entries):
        if  entries[num].config("text")[-1] == "0":
            entries[num].config(text = "1")
            entries[num].config(bg = "#00FF00")
        else: 
            entries[num].config(text = "0")
            entries[num].config(bg = "#FF0000")
    else:

        print(num-len(entries))

        if  topentries[num-len(entries)].config("text")[-1] == "0":
            topentries[num-len(entries)].config(text = "1")
            topentries[num-len(entries)].config(bg = "#00FF00")
        else: 
            topentries[num-len(entries)].config(text = "0")
            topentries[num-len(entries)].config(bg = "#FF0000")

def reset():
    # input bit buttons
    for i in range(0, 8):
        entries[i].config(text = "0")
        entries[i].config(bg = "#FF0000")

    # output led
    outputLEDLabel.config(bg = "#FF0000")

def create_top_window():

    top_window = Toplevel()
    top_window.geometry("400x400")
    top_window.title("Logic")
    top_window.resizable(False, False)
    top_window.configure(bg=bgColor)
    top_window.iconbitmap(os.path.join(sys.path[0], os.path.join("images", "Icon.ico")))

    toplogicButton = Button(top_window, width=2, bg=bgColor, justify="center")
    toplogicButton.grid(row=0, column=0, padx=(3,0), pady=(3,0))

    topbitCheck = Checkbutton(top_window, bg=bgColor)
    topbitCheck.grid(row=0, column=6, padx=(3,0), pady=(3,0))

    # put bit input buttons on screen
    window_two = top_window
    for i in range(0, len(topentries)):
        topentries[i].grid(row=2, column=i, pady=(5,0))




# GUI stuff
resetButton = Button(root, command=reset, width=5, text="Reset", bg=bgColor, justify="center")
resetButton.grid(row=0, column=0, columnspan=2, sticky="e", pady=(3,0))

stepButton = Button(root, command=step, width=5, text="Step", bg=bgColor, justify="center")
stepButton.grid(row=1, column=0, columnspan=2, sticky="e", pady=(3,0))

outputLabel = Label(root, text="Output:", bg=bgColor, justify="center")
outputLabel.grid(row=2, column=8, pady=(5,0))
outputLEDLabel = Label(root, width=2, bg="#FF0000", justify="center", borderwidth=2, relief="solid")
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
for i in range(0, len(entries)):
    entries[i].grid(row=2, column=i, pady=(5,0))

window_two = None

topentries = [
    Button(window_two, command=lambda:switch(len(entries)),   width=2, text="0", bg = "#FF0000", justify="center"),
    Button(window_two, command=lambda:switch(len(entries)+1), width=2, text="0", bg = "#FF0000", justify="center"),
    Button(window_two, command=lambda:switch(len(entries)+2), width=2, text="0", bg = "#FF0000", justify="center"),
    Button(window_two, command=lambda:switch(len(entries)+3), width=2, text="0", bg = "#FF0000", justify="center"),
    Button(window_two, command=lambda:switch(len(entries)+4), width=2, text="0", bg = "#FF0000", justify="center"),
]

# Hou onderaan
root.mainloop()