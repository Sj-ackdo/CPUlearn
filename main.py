# Imports
from tkinter import *
import os, sys

instruction = str()
register = int(0)
Xin = int(0)
Yin = int(0)
IEN = int(0)
OEN = int(0)
JMP = int(0)
RTN = int(0)
SKP = int(0) 
NOPO = int(0)
NOPF = int(0) 
def instructionset(instruction):
    global register; int(register)
    global Xin
    global Yin
    global IEN
    global OEN
    global JMP
    global RTN
    global SKP
    global NOPO
    global NOPF
    if instruction == "0000": # do nothing
        register = register
        if NOPO == 0:
            NOPO = 1
        elif NOPO == 1:
            NOPO = 0
    elif instruction == "0001": # Load in RR
        register = Xin
    elif instruction == "0010": # Store Complement (not)
        if Xin == 0:
            register = 1
        elif Xin == 1:
            register = 0
    elif instruction == "0011": # AND
        register = Xin * register
    elif instruction == "0100": # AND Complement
        if Xin == 1:
            register = 0 * register
        elif Xin == 0:
            register = 1 * register
    elif instruction == "0101": # OR
        if Xin == 1:
            if register == 1:
                register = 0
            elif register == 0:
                register = 1
        elif Xin == 0:
            if register == 1:
                register = 1
            elif register == 0:
                register = 0
    elif instruction == "0110": # OR Complement (NOR)
        if Xin & register == 1:
            register = 0
        elif Xin & register == 0:
            register = 1
    elif instruction == "0111": # XNOR
        if register == Xin:
            register = 1
        elif register != Xin:
            register = 0
    elif instruction == "1000": # Store command (Write)
        Yin = register
        Xin = register
    elif instruction == "1001": # Store Complement (Write)
        if register == 0:
            Yin = 1
            Xin = 1
        elif register == 1:
            Yin = 0 
            Xin = 0
    elif instruction == "1010": # Input Enable
        IEN = 1
    elif instruction == "1011": # Output Enable
        OEN = 1
    elif instruction == "1100": # JMP flag
        JMP = 1
    elif instruction == "1101": # Return flag
        RTN = 1
    elif instruction == "1110": # skip next instruct
        SKP = 1
    elif instruction == "1111": # flag f
        register = register
        if NOPF == 0:
            NOPF = 1
        elif NOPF == 1:
            NOPF = 0

# Window
bgColor = "#C3C3C3"

# create input file
# try:
#     with open(os.path.join(sys.path[0], "input.bin"), "w") as ifile:
#         pass
# except PermissionError:
#     print("Can't access file")


root = Tk()
root.geometry("400x300")
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
    global bit_states
    global Xin
    bit_states = []
    instr = ""

    for i in range(0, len(entries)):
        bit_states.append(entries[i].config("text")[-1])
        instr = instr + entries[i].config("text")[-1]

    print(bit_states)

    Xin = bit_states[len(bit_states)-1]

    instr = instr[:-1]

    print(instr)
    print(Xin)

    return instr


def clock_cycle():
    global Yin

    input = get_bit_states()
    print(input)

    instructionset(input)

    print(Yin)

    if Yin == 0:
        outputLEDLabel.config(bg = "#FF0000")
    elif Yin == 1:
        outputLEDLabel.config(bg = "#00FF00")




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

#     print("register value ", register) # verbonden aan vakje Reg. Value
#     print("data value ", Xin)          # Verbonden aan vakje Data value
#     print("output value ", Yin)        # Verbonden aan Output
#     print("o flag ", NOPO)             # verbonden aan vakje o flag
#     print("IEN value ", IEN)           # verbonden aan vakje In. Enable
#     print("OEN value ", OEN)           # verbonden aan vakje Out. Enable
#     print("JMP value ", JMP)           # verbonden aan vakje JMP flag
#     print("RNT value ", RTN)           # verbonden aan vakje RTN flag
#     print("SKP value ", SKP)           # verbonden aan vakje SKP flag
#     print("f flag ", NOPF)             # verbonden aan vakje f flag

registerLabel = Label(root, width=12, text="Register: ", anchor="w")
registerLabel.grid(row=2, column=0, columnspan=4, padx=(3,0), pady=(3,0), sticky="w")

dataLabel = Label(root, width=12, text="Data: ", anchor="w")
dataLabel.grid(row=3, column=0, columnspan=4, padx=(3,0), sticky="w")

oflagLabel = Label(root, width=12, text="O flag: ", anchor="w")
oflagLabel.grid(row=4, column=0, columnspan=4, padx=(3,0), sticky="w")

fflagLabel = Label(root, width=12, text="F flag: ", anchor="w")
fflagLabel.grid(row=5, column=0, columnspan=4, padx=(3,0), sticky="w")

inputLabel = Label(root, width=12, text="Input enabled: ", anchor="w")
inputLabel.grid(row=6, column=0, columnspan=4, padx=(3,0), sticky="w")

# Hou onderaan
root.mainloop()