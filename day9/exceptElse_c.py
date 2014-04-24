import sys

for arg in sys.argv[1:]
    print(arg)
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannont open ', arg)
    else:
        print(arg, 'has', len(f.readlines())), ' lines')
        f.close()

