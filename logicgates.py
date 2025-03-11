rx = 0
ry = 0 

rx = int(input())
ry = int(input())

def AND():
    if(rx and ry == 0):
        return 0
    elif(rx == 0 and ry == 1):
        return 0
    elif(rx == 1 and ry == 0):
        return 0
    elif(rx and ry == 1):
        return 1

def NAND():
    if(rx and ry == 1):
        return 0
    else:
        return 1  
    
def OR():
    if(rx and ry == 0):
        return 0
    else:
        return 1

def NOR():
    if(rx and ry == 0):
        return 1
    else:
        return 0
  
def XOR():
    if(rx == 0 and ry == 1):
        return 1
    if(rx == 1 and ry == 0):
        return 1
    else:
        return 0
    
def INV():
    if(rx or ry == 1):
        return 0
    if(rx or ry == 0):
        return 1

print(AND())