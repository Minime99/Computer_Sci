"""
Assignment
----------
"""

name = "Noah"

print(len(name))
# gives the length of name: 4
print(name.upper())
# prints out name in all upper case
print(name.lower())
# prints out name again in lower case

"""
SLICING
-------
"""
print(name[1:3])
# takes out from 1 to 3 in the array that is name: oa (does not give the third)
print(name[1:])
# goes on from 1 in the array and dosen't stop till the end

# List
x = ["apple", 2, True]
'''
order
can change
can have duplicates
'''
x.append()

# tuple
t = ()
'''
order
cant change
can have duplicates
'''
# set
s = {}
'''
no order
can be changed
cant have duplicates
'''
s.add()

# Dictionary
d = {key: value}
'''
no order but keys are always before values
can change
cant have duplicate keys, but different keys might have different values
'''
d["urine"] = 67


"""
FILE
----
"""
R = open("gulag.txt", "r")
R.close
# opens the file and prepares it for reading (for the file called gulag.txt)
W = open("file.txt", "w")
W.close
# opens the file and prepares it for writing (left like this the file will be
# empty)
A = open("file.txt", "a")
A.close
# opens the file and prepares it to add something on to the end of it

# if left "" will default to read

text = f.read()
# can assign something(text) to read a file

# EX:
"""
f = open("wall.txt","w")
f.write("5 feet higher")
f.close()
"""
# will replace what ever text is inside wall.txt with 5 feet higher


"""
IF/ELIF/ELSE
------------
"""
x = int(input("how old are you?"))

if x >= 19:
    print("you can hack darts")

elif x == 18:
    print("you can buy lotto, but not cigs")

else:
    print("you should leave")

"""
This wil get what you inputed for x and turn that into a int
after that python will check if it is greater then 19 if yes then something
will be printed.
If not then python will check if it is the same as 18 if yes then something
will be printed.
If both of these are not ture then it will print something that is different
then the other two options.
"""

# things that can check for truw and false
>=
>
<=
<
==
!=
