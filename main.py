# Imports
from tkinter import *
import os, sys
from logicgates import AND, NAND, OR, NOR, XOR, INV

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
root.geometry("256x225")
root.title("CPU")
root.resizable(False, False)
root.configure(bg=bgColor)
root.iconbitmap(os.path.join(sys.path[0], os.path.join("images", "Icon.ico")))

def switch(num):

    if  entries[num].config("text")[-1] == "0":
        entries[num].config(text = "1")
        entries[num].config(bg = "#00FF00")
    else: 
        entries[num].config(text = "0")
        entries[num].config(bg = "#FF0000")

def reset():
    for i in range(0, len(entries)):
        entries[i].config(text = "0")
        entries[i].config(bg = "#FF0000")

    outputLEDLabel.config(bg = "#FF0000")
    

def get_bit_states():
    global bit_states
    global Xin
    bit_states = []
    instr = ""

    for i in range(0, len(entries)):
        bit_states.append(entries[i].config("text")[-1])
        instr = instr + entries[i].config("text")[-1]

    Xin = int(bit_states[len(bit_states)-1])

    instr = instr[:-1]

    return instr

def clock_cycle():
    global register, Xin, Yin, NOPO, IEN, OEN, JMP, RTN, SKP, NOPF

    input = get_bit_states()
    instructionset(input)

    if Yin == 0:
        outputLEDLabel.config(bg = "#FF0000")
    elif Yin == 1:
        outputLEDLabel.config(bg = "#00FF00")

    registerLabel.config(text = "Register: " + str(register))
    dataLabel.config(text = "Data: " + str(Xin))
    oflagLabel.config(text = "O flag: " + str(NOPO))
    fflagLabel.config(text = "F flag: " + str(NOPF))
    inputLabel.config(text = "Input enabled: " + str(IEN))
    outputLabel.config(text = "Output enabled: " + str(OEN))
    jumpLabel.config(text = "JMP flag: " + str(JMP))
    rtnLabel.config(text = "RTN flag: " + str(RTN))
    skpLabel.config(text = "SKP flag: " + str(SKP))


# GUI stuff
# logicButton = Button(root, command=logic, width=6, text="Logic", bg=bgColor, justify="center")
# logicButton.grid(row=0, column=0, columnspan=2, padx=(3,0), pady=(3,0))

# bitLabel = Label(root, width=4, text="4-Bit:", bg="#00FF00", anchor="w")
# bitLabel.grid(row=0, column=9, padx=(23,0), pady=(3,0))

# bitCheck = Checkbutton(root, bg=bgColor)
# bitCheck.grid(row=0, column=10, pady=(3,0))

# logButton = Button(root, command=logic, width=6, text="Logic", bg=bgColor, justify="center")
# logButton.grid(row=0, column=11, columnspan=2, padx=(3,0), pady=(3,0))

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
outputLEDLabel.grid(row=1, column=len(entries)+5, padx=(7,0), pady=(5,0))

resetButton = Button(root, command=lambda:reset(), width=4, text="Reset", justify="center")
resetButton.grid(row=1, column=len(entries)+6, padx=(10,0), pady=(5,0))

registerLabel = Label(root, width=14, text="Register: 0", anchor="w", bg=bgColor)
registerLabel.grid(row=2, column=0, columnspan=4, padx=(3,0), pady=(3,0), sticky="w")

dataLabel = Label(root, width=14, text="Data: 0", anchor="w", bg=bgColor)
dataLabel.grid(row=3, column=0, columnspan=4, padx=(3,0), sticky="w")

oflagLabel = Label(root, width=14, text="O flag: 0", anchor="w", bg=bgColor)
oflagLabel.grid(row=4, column=0, columnspan=4, padx=(3,0), sticky="w")

fflagLabel = Label(root, width=14, text="F flag: 0", anchor="w", bg=bgColor)
fflagLabel.grid(row=5, column=0, columnspan=4, padx=(3,0), sticky="w")

inputLabel = Label(root, width=14, text="Input enabled: 0", anchor="w", bg=bgColor)
inputLabel.grid(row=6, column=0, columnspan=4, padx=(3,0), sticky="w")

outputLabel = Label(root, width=14, text="Output enabled: 0", anchor="w", bg=bgColor)
outputLabel.grid(row=7, column=0, columnspan=4, padx=(3,0), sticky="w")

jumpLabel = Label(root, width=14, text="JMP flag: 0", anchor="w", bg=bgColor)
jumpLabel.grid(row=8, column=0, columnspan=4, padx=(3,0), sticky="w")

rtnLabel = Label(root, width=14, text="RTN flag: 0", anchor="w", bg=bgColor)
rtnLabel.grid(row=9, column=0, columnspan=4, padx=(3,0), sticky="w")

skpLabel = Label(root, width=14, text="SKP flag: 0", anchor="w", bg=bgColor)
skpLabel.grid(row=10, column=0, columnspan=4, padx=(3,0), sticky="w")

stepButton = Button(root, command=clock_cycle(), width=6, text="Step", justify="center")
stepButton.grid(row=1, column=len(entries)+7, padx=(3,0), pady=(5,0))
# end cpu
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# logic window stuff
logicroot = Tk()
logicroot.geometry("208x80")
logicroot.title("Logic")
logicroot.resizable(False, False)
logicroot.configure(bg=bgColor)
logicroot.iconbitmap(os.path.join(sys.path[0], os.path.join("images", "Icon.ico")))

def logicswitch(num):

    if  logicentries[num].config("text")[-1] == "0":
        logicentries[num].config(text = "1")
        logicentries[num].config(bg = "#00FF00")
    else: 
        logicentries[num].config(text = "0")
        logicentries[num].config(bg = "#FF0000")

def logicreset():
    for i in range(0, len(logicentries)):
        logicentries[i].config(text = "0")
        logicentries[i].config(bg = "#FF0000")

    logicoutputLEDLabel.config(bg = "#FF0000")
    

def logicget_bit_states():
    global logicbit_states
    logicbit_states = []

    for i in range(0, len(logicentries)):
        logicbit_states.append(logicentries[i].config("text")[-1])


def go_through_logic_gate():
    logicget_bit_states()
    gate = curGate.get()
    if gate == "AND":
        output = AND(logicbit_states[0], logicbit_states[1])
    if gate == "NAND":
        output = NAND(logicbit_states[0], logicbit_states[1])
    if gate == "OR":
        output = OR(logicbit_states[0], logicbit_states[1])
    if gate == "NOR":
        output = NOR(logicbit_states[0], logicbit_states[1])
    if gate == "XOR":
        output = XOR(logicbit_states[0], logicbit_states[1])
    if gate == "INV":
        output = INV(logicbit_states[0], logicbit_states[1])

    print(output)

    if output == 0:
        logicoutputLEDLabel.config(bg = "#FF0000")
    elif output == 1:
        logicoutputLEDLabel.config(bg = "#00FF00")

# bit input buttons
logicbit_states = []

logicentriesFrame = Frame(logicroot)

logicentries = [
    Button(logicentriesFrame, command=lambda:logicswitch(0), width=2, bg="#FF0000", text="0", justify="center"),
    Button(logicentriesFrame, command=lambda:logicswitch(1), width=2, bg="#FF0000", text="0", justify="center"),
]

# put bit input buttons on screen
for i in range(0, len(logicentries)):
    logicentries[i].pack(side=LEFT)

logicentriesFrame.grid(row=1, column=0, columnspan=len(logicentries), padx=(3,0), pady=(5,0))

logicoutputLEDLabel = Label(logicroot, width=2, bg="#FF0000", borderwidth=2, relief="solid")
logicoutputLEDLabel.grid(row=1, column=len(logicentries)+5, padx=(7,0), pady=(5,0))

logicresetButton = Button(logicroot, command=lambda:logicreset(), width=4, text="Reset", justify="center")
logicresetButton.grid(row=1, column=len(logicentries)+6, padx=(10,0), pady=(5,0))

logicgates = [
    "AND", 
    "NAND", 
    "OR", 
    "NOR", 
    "XOR", 
    "INV"
]


curGate = StringVar(logicroot)
curGate.set(logicgates[0])
gateMenu = OptionMenu(logicroot, curGate, *logicgates)
gateMenu.config(highlightbackground=bgColor, width=5, anchor="w")
gateMenu.grid(row=2, column=0, columnspan=3, pady=(3,0))

logicstepButton = Button(logicroot, command=go_through_logic_gate(), width=6, text="Step", justify="center")
logicstepButton.grid(row=1, column=len(logicentries)+7, padx=(3,0), pady=(5,0))

# Hou onderaan
root.mainloop()
logicroot.mainloop()