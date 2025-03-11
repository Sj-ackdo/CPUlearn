# def instructionset(instruction):
#     av_ins = {
#         "0000": ""
#     }
#     return av_ins.get(instruction, "not in instructionset")
instruction = int(0o1)
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
            register = Xin
            print(register)
            print(Xin) 
    
instructionset(0o10)  
