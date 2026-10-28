n=int(input("enter distance: "))
period=input("day or night: ")

if period=="day":
    if n<20:
        p=33.58+37.89*n
        print("Taxi :",p)
    elif n<100:
        p=4.32*n
        print("Bus :",p)
    else:
        p=2.88*n
        print("Train :",p)
elif period=="night":
    if n<20:
        p=33.58+43.17*n
        print("Taxi :",p)
    elif n<100:
        p=4.32*n
        print("Bus :",p)
    else:
        p=2.88*n
        print("Train :",p)