try:
    x = input("what's your name?")
    x +=1
    print(x)

except(RuntimeError, TypeError, NameError):
    pass

print("it totally didn't cause a crash")
