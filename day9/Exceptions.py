while True:
    try:
        x = int(input("please enter a number"))
        break
        #when this happens the program stops (because it breaks you out of the while loop and there's nothing else in this code!)

    except ValueError:
        print("Ophs that was no valid number")

