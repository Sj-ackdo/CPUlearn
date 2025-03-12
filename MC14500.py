# def instructionset(instruction):
#     av_ins = {
#         "0000": ""
#     }
#     return av_ins.get(instruction, "not in instructionset")
instruction = str()
Xin = int()
register = int()

def instructionset(instruction):
    global register
    global Xin
    global Yin
    if instruction == "0000": # do nothing
        register = register
        NOPO = 1
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
    elif instruction == "1001": # Store Complement (Write)
        if register == 0:
            Yin = 1
        elif register == 1:
            Yin = 0
    elif instruction == "1010": # Input Enable
        IEN = 1
    elif instruction == "1011": # Output Enable
        OEN = 1
    elif instruction == "1100": # JMP flag
        JMP = 1
    elif instruction == "1101": # Return flag
        RNT = 1
    elif instruction == "1110": # skip next instruct
        SKP = 1
    elif instruction == "1111": # flag f
        register = register
        NOPF = 1    

x = str()

while x != "STOP":
    Xin = int(input())
    inputs = input("Instruction:")
    instructionset(inputs)
    print("register value", register)
    print("data value", Xin)
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