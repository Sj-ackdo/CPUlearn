# def instructionset(instruction):
#     av_ins = {
#         "0000": ""
#     }
#     return av_ins.get(instruction, "not in instructionset")
instruction = int()
register = int()
Xin = int(1)
Yin = int()


def instructionset(instruction):
    global register
    global Xin
    global Yin
    if instruction == 0o0: # do nothing
        register = register
    elif instruction == 0o1: # Load in RR
        register = Xin
    elif instruction == 0o10: # NOT (Store complemenet)
        if Xin == 0:
            register = 1
        elif Xin == 1:
            register = 0
    elif instruction == 0o11: # AND
        register = Xin * register
    elif instruction == 0o100: # AND Complement
        if Xin == 1:
            register = 0 * register
        elif Xin == 0:
            register = 1 * register
    elif instruction == 0o101: # OR
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
    elif instruction == 0o110:
        

    else:
        register = "not in instructionset"
    return register

# DEBUG
print("Register:", register)
print("Xin:", Xin)

instructionset(0o1)
print("Register:", register)
print("Xin:", Xin)

instructionset(0o11)
print("Register", register)
print("Xin", Xin)