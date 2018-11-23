f = open('totc.txt', 'r')                   #This opens the Tale of Two Cities txt (totc.txt) document in the Quiz Files folder
text = f.read()                             #This reads what is in the file
text2 = text.upper()                        #This makes everything in the file uppercase
f.close()                                   #This closes the file

d = open('upper.txt', 'w')                  #This creates a new file called upper.txt   It is opened in write mode
d.write(text2)                              #This makes upper.txt to contain everything in totc.txt uppercase version
d.close()                                   #This closes upper.txt

b = open('upper.txt', 'a')                  #This opens upper.txt in append mode
b.write('New Line at the end')              #This writes this line at the end of the upper.txt
b.close()                                   #This closes upper.txt
