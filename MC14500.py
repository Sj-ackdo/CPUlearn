# def instructionset(instruction):
#     av_ins = {
#         "0000": ""
#     }
#     return av_ins.get(instruction, "not in instructionset")
instruction = int(0o1)
global register
register = int()
Xin = int(1)
Yin = int()


def instructionset(instruction):
    match instruction:
        case 0000:
           pass
        case 0o1:
            register = Xin
        case 0o10:
            if(Xin == 1):
                register == 0
            elif(Xin == 0):
                register == 1
        case 0o11:
            register = register * Xin
    
instructionset(0o1)
instructionset(0o11)  
print(register)
print(Xin)
