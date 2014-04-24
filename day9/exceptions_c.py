while True:
    try:
        x = int(input("please enter a number"))
        break
        #when this happens the program stops

    except ValueError:
        print("Ophs that was no valid number")
print("i'm now here")
