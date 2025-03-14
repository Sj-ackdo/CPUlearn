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
root.geometry("400x150")
root.title("CPU")
root.resizable(False, False)
root.configure(bg=bgColor)
root.iconbitmap(os.path.join(sys.path[0], os.path.join("images", "Icon.ico")))

# Functions
def main():
    pass

def switch(num):

    if  entries[num].config("text")[-1] == "0":
        entries[num].config(text = "1")
        entries[num].config(bg = "#00FF00")
    else: 
        entries[num].config(text = "0")
        entries[num].config(bg = "#FF0000")

def logic():
    create_top_window()

def create_top_window():

    top_window = Toplevel()
    top_window.geometry("250x150")
    top_window.title("Logic")
    top_window.resizable(False, False)
    top_window.configure(bg=bgColor)
    top_window.iconbitmap(os.path.join(sys.path[0], os.path.join("images", "Icon.ico")))

def reset():
    for i in range(0, len(entries)):
        entries[i].config(text = "0")
        entries[i].config(bg = "#FF0000")

def get_bit_states():
    for i in range(0, len(entries)):
        bit_states.append(entries[i].config("text")[-1])
        print(bit_states)

def clock_cycle():
    get_bit_states()





# GUI stuff
logicButton = Button(root, command=logic, width=6, text="Logic", bg=bgColor, justify="center")
logicButton.grid(row=0, column=0, columnspan=2, padx=(3,0), pady=(3,0))

bitLabel = Label(root, width=4, text="4-Bit:", bg="#00FF00", anchor="w")
bitLabel.grid(row=0, column=9, padx=(23,0), pady=(3,0))

bitCheck = Checkbutton(root, bg=bgColor)
bitCheck.grid(row=0, column=10, pady=(3,0))

logButton = Button(root, command=logic, width=6, text="Logic", bg=bgColor, justify="center")
logButton.grid(row=0, column=11, columnspan=2, padx=(3,0), pady=(3,0))

# bit input buttons
bit_states = []

entriesFrame = Frame(root)

entries = [
    Button(entriesFrame, command=lambda:switch(0), width=2, bg="#FF0000", text="0", justify="center"),
    Button(entriesFrame, command=lambda:switch(1), width=2, bg="#FF0000", text="0", justify="center"),
    Button(entriesFrame, command=lambda:switch(2), width=2, bg="#FF0000", text="0", justify="center"),
    Button(entriesFrame, command=lambda:switch(3), width=2, bg="#FF0000", text="0", justify="center"),
    Button(entriesFrame, command=lambda:switch(4), width=2, bg="#FF0000", text="0", justify="center")
]

# put bit input buttons on screen
for i in range(0, len(entries)):
    entries[i].pack(side=LEFT)

entriesFrame.grid(row=1, column=0, columnspan=len(entries), padx=(3,0), pady=(5,0))

outputLEDLabel = Label(root, width=2, bg="#FF0000", borderwidth=2, relief="solid")
outputLEDLabel.grid(row=1, column=len(entries)+5, padx=(5,0), pady=(5,0))

resetButton = Button(root, command=lambda:reset(), width=4, bg=bgColor, text="Reset", justify="center")
resetButton.grid(row=1, column=len(entries)+6, padx=(20,0), pady=(5,0))

stepButton = Button(root, command=clock_cycle, width=6, bg=bgColor, text="Step", justify="center")
stepButton.grid(row=1, column=len(entries)+7, padx=(3,0), pady=(5,0))

# Hou onderaan
root.mainloop()