import datetime
inv = {"Common nails": 11, "Box nails": 5, "Drywall nails": 20,
       "Double headed nails": 2, "Roofing nails": 13}


def saveinv():
    x = open("/Users/noahfedosoff_S/Documents/Projects/Project(inv.control)/inv.txt", "w")
    s = str(inv)
    x.write(s)
    x.close()


def editinv(e):
    x1 = open("/Users/noahfedosoff_S/Documents/Projects/Project(inv.control)/inv.txt", "a")
    x1.write(e)


c = input("what are you going to add to the inv?")
editinv(c)


def readinv():
    x2 = open("/Users/noahfedosoff_S/Documents/Projects/Project(inv.control)/inv.txt", "r")
    print(x2.read())


doyouwanttime = input("do you want the time? [y,n]")
if doyouwanttime == "y":
    x = datetime.datetime.now()
    print(x)
