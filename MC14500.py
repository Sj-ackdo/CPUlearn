import os

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

def resetCount():
    global register, Xin, Yin, IEN, OEN, JMP, RTN, SKP, NOPO, NOPF
    #Xin = 0
    Yin = 0
    IEN = 0
    OEN = 0
    JMP = 0
    RTN = 0
    SKP = 0
    #NOPO = 0
    #NOPF = 0

x = str()
os.system("cls")
Xin = int(input())
while x != "STOP":
    inputs = input("Instruction: ")
    os.system("cls")
    if inputs == "q":
        quit()
    instructionset(inputs)             # Wat ik wil met de volgende value's : een tekstvak met een 1 / 0 in een vakje ernaast.  ->> instructionset(inputs) wordt gecalled als step button
    print("register value ", register) # verbonden aan vakje Reg. Value
    print("data value ", Xin)          # Verbonden aan vakje Data value
    print("output value ", Yin)        # Verbonden aan Output
    print("o flag ", NOPO)             # verbonden aan vakje o flag
    print("IEN value ", IEN)           # verbonden aan vakje In. Enable
    print("OEN value ", OEN)           # verbonden aan vakje Out. Enable
    print("JMP value ", JMP)           # verbonden aan vakje JMP flag
    print("RNT value ", RTN)           # verbonden aan vakje RTN flag
    print("SKP value ", SKP)           # verbonden aan vakje SKP flag
    print("f flag ", NOPF)             # verbonden aan vakje f flag
    resetCount()
    x = "RUN"

# # DEBUG
# print("Register:", register)
# print("Xin:", Xin)

# instructionset(0o1)
# print("Register:", register)
# print("Xin:", Xin)

# instructionset(0o11)
# print("Register", register)
# print("Xin", Xin)