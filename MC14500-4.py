instruction = str()
register = int(0)
Xin = int(0)
Yout = int(0)
IEN = int(0)
OEN = int(1)
JMP = int(0)
RTN = int(0)
SKP = int(0) 
NOPO = int(0)
NOPF = int(0) 
storereg = int(0)
# RegA = int(0)
# RegB = int(0)
# RegC = int(0)
# RegD = int(0)

def instructionset(instruction):
    global register
    global Xin
    global Yout
    global IEN
    global OEN
    global JMP
    global RTN
    global SKP
    global NOPO
    global NOPF
    global storereg
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
    elif instruction == "1000": # Store command (Write) ---> on store move to next register (RegA -> RegB -> RegC -> RegD) 
        if OEN == 1:
            Yout = register
            Xin = register
            storereg = storereg + 0b1
    elif instruction == "1001": # Store Complement (Write)
        if OEN == 1:    
            if register == 0:
                Yout = 1
                Xin = 1
                storereg = storereg + 0b1
            elif register == 1:
                Yout = 0 
                Xin = 0
                storereg = storereg + 0b0
    elif instruction == "1010": # Input Enable
        if IEN == 1:
            IEN = 0
        elif IEN == 0:
            IEN = 1
    elif instruction == "1011": # Output Enable
        if OEN == 1:
            OEN = 0
        elif OEN == 0:
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

inputs = input()
instructionset(inputs)
print(register)
print(Xin)
print(int(storereg))

# / in 4-bit mode -> RR ($register) counts as carry flag
# |-> IEN / OEN == Output / Input Enable --> Door de 1-bit bus met 4-bit input / output moet er getoggled worden tussen input en output
# |-> SKP flag -> Skip next instruction if RR = 0
# |-> JMP flag -> Jump to specified instruction --> not supported until scripting is supported
# |-> RTN flag -> Skip next instruction
# |-> NOPF / NOPO flag -> no use yet