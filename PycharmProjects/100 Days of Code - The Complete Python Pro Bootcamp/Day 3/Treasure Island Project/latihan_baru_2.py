lamp = input("lamp plugged in? yes or no: ")
if lamp == "yes":
    lamp = input("bulb burned out? yes or no: ")
    if lamp == "yes":
        print("replace bulb!")
    else:
        print("repair lamp!")
else:
    print("plug in lamp")