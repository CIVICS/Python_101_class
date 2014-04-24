def logicalAnd(s):
    wordOne = "cat"
    wordTwo = "mouse"
    for eachChar in s:
        if(s != 'a' and s != 'b'):
            print( wordOne + wordTwo)

print(logicalAnd("compsci"))
print(logicalAnd("aAbEefIijOopUus"))
