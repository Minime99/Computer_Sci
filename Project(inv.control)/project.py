
import datetime
inv = {"Common nails": 11, "Box nails": 5, "Drywall nails": 20,
       "Double headed nails": 2, "Roofing nails": 13}


def saveinv():
    x = open("/Users/noahfedosoff_S/Documents/Projects/Project(inv.control)/inv.txt", "w")
    s = str(inv)
    x.write(s)
    x.close()


saveinv()


def editinv(e):
    x1 = open("/Users/noahfedosoff_S/Documents/Projects/Project(inv.control)/inv.txt", "a")
    x1.write(e)
    x1.close()


c = input("what are you going to add to the inv?")
editinv(c)

r = input("do you want to see the new inv? [y,n]")
if r == "y":
    v = open("/Users/noahfedosoff_S/Documents/Projects/Project(inv.control)/inv.txt", "r")
    print(v.read())
    v.close()


doyouwanttime = input("do you want the time? [y,n]")
if doyouwanttime == "y":
    x = datetime.datetime.now()
    print(x)

n = input("can you see the inv ok? [y,n]")
if n == "n":
    p = open("/Users/noahfedosoff_S/Documents/Projects/Project(inv.control)/inv.txt", "r")
    print(p.read().upper())
    p.close()
