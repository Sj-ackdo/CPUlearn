control = 0
data = 0

def AND(rx, ry):
    if(rx and ry == 0):
        return 0
    elif(rx == 0 and ry == 1):
        return 0
    elif(rx == 1 and ry == 0):
        return 0
    elif(rx == 1 and ry == 1):
        return 1

def NAND(rx, ry):
    if(rx and ry == 1):
        return 0
    else:
        return 1  
    
def OR(rx, ry):
    if(rx and ry == 0):
        return 0
    else:
        return 1

def NOR(rx, ry):
    if(rx and ry == 0):
        return 1
    else:
        return 0
  
def XOR(rx, ry):
    if(rx == 0 and ry == 1):
        return 1
    if(rx == 1 and ry == 0):
        return 1
    else:
        return 0
    
def INV(rx, ry):
    if(rx or ry == 1):
        return 0
    if(rx or ry == 0):
        return 1
    
# def TRIBUF():
#     if(data == 1 and control == 0):
#         return 0
#     if(data == 0 and control == 1):
#         return 0
#     if(data == 1 and control == 1):
#         return 1
#     if(data == 0 and control == 0):
#         return 0