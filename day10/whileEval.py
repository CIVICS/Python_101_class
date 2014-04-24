def sumTo(abounds):
    """Return the sum of 1+2+3...n"""
    theSum = 0
    aNumber = 1
    while aNumber <= abounds:
        theSum = theSum +aNumber
        aNumber = aNumber +1
    return theSum

print(sumTo(4))
#how to display docString
#1. in interactive mode
#2 more commonly in code

print(sumTo.__doc__)
#this technique works with builtin functions as well as modules and classes
print(help(print))
#from command line type import this
#this is python's philosophy


