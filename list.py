thislist = ["apple", "banana", "cherry"]  # A list is a collection which is ordered and changeable.

print(len(thislist))  # this will say how many are in the list

for x in thislist:  # prints everthing inside the list
    print(x)

# tuples are like lists but cannot be changed #a=(1,2,3)
# sets are an unordered collection of unique elements #x = set ([3,1,2,1])
# dictionaries are unordered, changeable and indexed
# rain_percent = {1980:'17%',1981:'15%'}
# print (rain_percent) lists off everthing
# print (rain_percent[1980]) makes it so it will only look up 1980

thisdict = {"jake": 'taub', "sonny": 'farber'}
x = input("what is your name?")
if x in thisdict:
    print(thisdict[x])
else:
    print("who are you?")
