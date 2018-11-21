# opens the tale of new cities book
x = open("/Users/noahfedosoff_S/Documents/Projects/tale.txt", "r")
g = x.read().upper()  # sets g to be the tale of two cities file put into upper case
c = open("upper.txt")  # makes a new file called upper.txt
f = open("/Users/noahfedosoff_S/Documents/Projects/upper.txt",
         "w+")  # opens the new txt file in writeplus mode
f.write(g)  # writes out the tale of new cities book in upper
# open the upper .txt again and in append mode
a = open("/Users/noahfedosoff_S/Documents/Projects/upper.txt", "a")
print(a.write("ok new"))  # adds ok new to the end of the file
# proves it is their as making a new file returns an error if it is already their
v = open("upper.txt", "x")

f.close()  # close all the opened files
x.close()
c.close()
a.close()
v.close()
