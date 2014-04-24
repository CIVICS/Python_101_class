#this function squares numbers
mylist = [1,2,3,4,5]

yourlist = [item ** 2 for item in mylist]

print(yourlist)
#The expression describes each element of the list that is being built.
#The for clause iterates thru each item in a sequence.
#The items are filtered by the if clause if there is one.
