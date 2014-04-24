file = open('aliceInWonderland.txt', 'r')
#opens a file and specfies we will use it for reading.

writeFile = open('aliceInWonderland.txt', 'w')
# Open a file called filename and use it for writing. returns a reference to a file object.

print(writeFile)
file.close()
#closes our file
