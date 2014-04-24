import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())

except IOError as err:
    print("i/o error: (0)" .format(err))
# as err assigned the error that was rasised to the variable err is there so usually so code can inspect it further
except ValueError as err:
    print("could not convert data into an int")
except:
    print("unexpected error", sys.exc_info()[0])
    raise
#raise here just re-raise the exception. so it's as if the orginial exception had been raised from this point onward. you'd need a case to catch it if you don't want the program to hault
