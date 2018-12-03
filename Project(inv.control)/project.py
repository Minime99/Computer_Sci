import datetime
import matplotlib
import matplotlib.pyplot as plt  # all of the imports to run the code, for showing the time and making the graph

inv = {"Common nails": 11, "Box nails": 5, "Drywall nails": 20,  # the starting inventory
       "Double headed nails": 2, "Roofing nails": 13}
print(inv)  # shows the user the starting inventory

x3 = open("/Users/noahfedosoff_S/Documents/Projects/Project(inv.control)/inv.txt",
          "w")  # makes a file called inv.txt
x3.close()  # close this open section


def saveinv():  # the def to save the starting inventory to inv.txt
    x = open("/Users/noahfedosoff_S/Documents/Projects/Project(inv.control)/inv.txt",
             "w+")  # opens the inv.txt file in write plus mode
    s = str(inv)  # sets the s to be the starting inventory as a string
    x.write(s)  # writes the starting inventory as a string to inv.txt
    x.close()  # close this open section


saveinv()  # runs the saveinv def


def editinv(e):  # the def to edit the starting inv inside the inv.txt file by adding e
    x1 = open("/Users/noahfedosoff_S/Documents/Projects/Project(inv.control)/inv.txt",
              "w")  # opens the inv.txt file in write mode
    x1.write(e)  # writes what ever e is set to too the inv.txt file
    x1.close()  # close this open section


# sets the fist value of the new item in the inv
c = input("what is the name of what you want to add to the inv?")
# sets the second value in the new item in the inv as an int
y1 = int(input("what is the amount you are adding"))
inv[c] = y1  # makes the new item in the inv
# adds this new item to the inv in the file using the editinv def based on inv[c]=y1
editinv(str(inv))

# input to decide if the user wants to see the new inv with the item added or not
r = input("do you want to see the new inv? [y,n]")
if r == "y":  # sets what happens if the user sets the input to y
    # if the user sets the input to y , this open will read out the file to the user
    v = open("/Users/noahfedosoff_S/Documents/Projects/Project(inv.control)/inv.txt", "r")
    print(v.read())  # prints out the file after the new itm is added by the user
    v.close()  # close this open section

# input to decide if the user wants to be able to see the new inv better
n = input("can you see the inv ok? [y,n]")
if n == "n":  # sets what happens if the user enters n
    # if the user does enter n this open will open the inv and print out the file in upper case
    p = open("/Users/noahfedosoff_S/Documents/Projects/Project(inv.control)/inv.txt", "r")
    print(p.read().upper())  # reads out the file in upper case using the new inv set by the user
    p.close()  # close this open section

# input to decide if the user wants to save this new inv to a new file called newinv.txt
x2 = input("do you want to save this inv.? [y,n]")
if x2 == "y":  # sets what happens if the user inputs y
    # if the user inputs y this open will write the new inv as a string to the newinv.txt file
    v1 = open("/Users/noahfedosoff_S/Documents/Projects/Project(inv.control)/newinv.txt", "w")
    v1.write(str(inv))  # adds in the new inv as a string to the file
    v1.close()  # close this open section
    print("saved as newinv.txt")  # lets the user know the inv has been saved

# input to decide if the user wants to know the current time
doyouwanttime = input("do you want the time? [y,n]")
if doyouwanttime == "y":  # sets what happens if the user enters y
    x = datetime.datetime.now()  # sets x to be the current time
    print(x)  # prints out the current time if the user inputed y

# input to decide what happens if the user wants a graph
g2 = input("do you want a graph of the new inv? [y,n]")
if g2 == "y":
    plt.bar(range(len(inv)), list(inv.values()), align='center')
    plt.xticks(range(len(inv)), list(inv.keys()))
    plt.show()

print("program ended")  # tells the user the program is over
