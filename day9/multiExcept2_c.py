import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as err:
    print("i/o error:(0)")
except ValueError as err:
    print("cound not convert data to int" )
except:
    print("unexpected error")
    raise

