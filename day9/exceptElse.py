import sys

for arg in sys.argv[1:]:
    print(arg)
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


#this script runs python from your cmd line and you can pass in argumens
# note we are doing some voodoo in the first line [1:] means get the second argument because the first argument is always the file's name
