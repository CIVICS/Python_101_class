from pythonds.basic.stack import Stack
#to instal this lib go to the link
# https://github.com/bnmnetp/pythonds
#extract the zip and place it in your python33/Lib folder named pythonds. You will need to remove the -master from the file name after extraction

rStack = Stack()

def toStr(n,base):
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n // base
    res = ""
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res

print(toStr(1453,16))
