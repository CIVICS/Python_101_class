#simple for
for f in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
    print("Hi", f, "Please come to my party on Saturday")
#for with accumulator pattern

def sumTo(abound):
    theSum = 0
    for aNumber in range (1, abound+1):
        theSum = theSum + aNumber
        return theSum
        print(theSum)


sumTo(5)
