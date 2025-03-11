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
    
print(AND())