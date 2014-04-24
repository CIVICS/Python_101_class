# def listSum(numList):
#     theSum = 0
#     for i in numList:
#         theSum = theSum+i
#     return theSum

# print(listSum([1,1,2,3,5,8,13]))

#1 the function will call itself
#2 must have an exit condition
# conditional check

def listsum(numList):
    if len(numList)==1:
        return numList[0]
    else:
        return numList[0] / listsum(numList[1:])
print(listsum([1,3,5,7,9]))
