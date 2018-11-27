
import datetime
import matplotlib
import matplotlib.pyplot as plt

inv = {"Common nails": 11, "Box nails": 5, "Drywall nails": 20,
       "Double headed nails": 2, "Roofing nails": 13}
print(inv)

x3 = open("/Users/noahfedosoff_S/Documents/Projects/Project(inv.control)/inv.txt", "w")
x3.close()


def saveinv():
    x = open("/Users/noahfedosoff_S/Documents/Projects/Project(inv.control)/inv.txt", "w+")
    s = str(inv)
    x.write(s)
    x.close()


saveinv()


def editinv(e):
    x1 = open("/Users/noahfedosoff_S/Documents/Projects/Project(inv.control)/inv.txt", "w")
    x1.write(e)
    x1.close()


c = input("what is the name of what you want to add to the inv?")
y1 = int(input("what is the amount you are adding"))
inv[c] = y1
editinv(str(inv))

r = input("do you want to see the new inv? [y,n]")
if r == "y":
    v = open("/Users/noahfedosoff_S/Documents/Projects/Project(inv.control)/inv.txt", "r")
    print(v.read())
    v.close()

n = input("can you see the inv ok? [y,n]")
if n == "n":
    p = open("/Users/noahfedosoff_S/Documents/Projects/Project(inv.control)/inv.txt", "r")
    print(p.read().upper())
    p.close()

x2 = input("do you want to save this inv.? [y,n]")
if x2 == "y":
    v1 = open("/Users/noahfedosoff_S/Documents/Projects/Project(inv.control)/newinv.txt", "w")
    v1.write(str(inv))
    v1.close()
    print("saved as newinv.txt")

doyouwanttime = input("do you want the time? [y,n]")
if doyouwanttime == "y":
    x = datetime.datetime.now()
    print(x)

g2 = input("do you want a graph of the new inv? [y,n]")
if g2 == "y":
    plt.bar(range(len(inv)), list(inv.values()), align='center')
    plt.xticks(range(len(inv)), list(inv.keys()))
    plt.show()
