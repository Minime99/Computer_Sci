#Final Neutered Version         :(

import math
import numpy
import random
import matplotlib
import datetime
import os
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#^Everything above this imports librarys of functions

while(True):                                                    #This creates a loop that asks the user for input.
    print('Booting Up Voter Database')                          #Their input determines what the program will do.
    print('Here are your options')
    print('1) Print the voter list')
    print('2) Find the locations of each voter')
    print('3) Learn who people voted for')
    print('4) View graphs of results')
    print('5) Find the time when a President is confirmed')
    print('5) View full results')
    print('6) Exit Program')
    x = input('What is your choice?')                           #This is where it is asked

    if x == '1':                                                #If the user inputs '1', this set of actions will be performed
        f = open('voters.txt', 'r+')                            #This opens the 'voters.txt' file in read and write
        text = f.read()                                         #This reads the file
        text = text.title()                                     #This capitalizes everyword in the file
        f.write(text.upper())                                   #This makes every letter uppercase
        print(text)                                             #This prints the list of names in the file

    if x == '4':                                                #If the user inputs '4', this set of actions will be performed
        location = ['North','South','Trump', 'Clinton']         #This determines what the four bars are in the bar graph
        location1 = [0.65,0.35,0.35,0.65]                       #This determines the possible percentages of each bar
        bar = matplotlib.pyplot.bar(location, location1, label = 'Voters')       #This line dictates how the numbers, location, and possible presidents interact with eachother. any of the 'location' items are then given values by the 'location1' items.
        matplotlib.pyplot.title('Voter Database')               #This determines what the title of the graph will be called.
        matplotlib.pyplot.ylabel('Number of Votes')             #This determines what the y axis is called.
        matplotlib.pyplot.xlabel('President Voter Locations')   #This determines what the x axis is called.
        matplotlib.pyplot.show()                                #This shows the graph
        break

    if x == '5':                                                #If the user inputs '5', this set of actions will be performed
        x = datetime.datetime.now()                             #This asks what the time is right now
        print('The President will be inaugurated at', x)        #This prints a string that tells when the president is inaugurated.
        break

    else:                                                       #This stops the program if they press a button that is not one of the designated numbers.
        break




#Old voter database that is too complicated
'''Voter Database'''

''' pseudo code v1.2

make a dictionary of random first names and last names with two possible locations on a txt document


class president:
    open the dictionary, read it, and print them out
    function that randomizes the first names, last names, and locations per person
    function that defines how many voters in total and then splits the voters in two between 40% and 60% per candidate
    function that will say the names of voters and where they are from (random names + north or south)

    ^This is old
options:
    function that opens the voter list and prints it out
    function that prints out number of voters
    function that makes every word in the list capitalized
    function that gives locations to each person
    function that splits the voters between 40% and 60% per candidate and says voted for trump or clinton


Object trump
make trump gets higher always percentage of southern voters

object clinton
make clinton gets higher always percentage of northern voters

string formatting stuff
make the printed list of every person have upper case names

matplotlib stuff
print out graphs of the amount of people voting for trump or clinton
prints out where the majority of people voted for a specific candidate

datetime stuff
print out time when a president wins
print out time when president is comfirmed (20 days at 12pm)



f = open('voters.txt', 'r+')
text = f.read()
text = text.title()
f.write(text)
f.close()


cd Desktop/Atom/'Computer_Sci.'/'Unit4(b_noah)'/'Business Application Project'
python3 'Business Application Project.py'
'''
'''
import math
import numpy
import random
import matplotlib
import datetime
import os
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

code v2 (No longer working)
while(True):
    print('Booting Up Voter Database')
    print('Here are your options')
    print('1) Print the voter list')
    print('2) Find the locations of each voter')
    print('3) Learn who people voted for')
    print('4) View graphs of results')
    print('5) Find the time when a President is confirmed')
    print('5) View full results')
    print('6) Exit Program')
    x = input('What is your choice?')

    if x == '1':
        f = open('voters.txt', 'r+')
        text = f.read()
        text = text.title()
        f.write(text)
        print('voters.txt')
        f.close()

    elif x == '2':
        f = open('voters.txt', 'r+')
        text = f.read()
        text = text.title()
        f.write(text)
        text.append(', North' or ', South')
        f.write(text)
        print('voters.txt')
        f.close()

    elif x == '3':
        f = open('voters.txt', 'r+')
        text = f.read()
        text = text.title()
        f.write(text.upper())
        '''
'''
        if random.randint(1,100)<50:
            text = text + ', North'
        else:
            text = text + ', South'
            if text.count(', North')>0:
                if random.randint(1,100)<66:
                    text = text + ', voted for Clinton'
            if text.count(', South')>0:
                if random.randint(1,100)<66:
                    text = text + ', voted for Trump'
        print('voters.txt')
        f.write(text)
        '''
'''
        f.close()

    else:
        break
#Graphs

'''
'''
pseudo code graphs
Stacked bar graph of who wins by votes
Bar graph of people from north or south
Bar graph of people and their locations percentage of who they voted for

Figure out a way to use the information from the previously performed function (1-3)
'''




'''
extra
    if x == 4:

A = [5., 30., 45., 22.]
B = [5., 25., 50., 20.]

X = range(4)

plt.bar(X, A, color = 'b')
plt.bar(X, B, color = 'r', bottom = A)
plt.show()


    if x == 4:
        t1 = numpy.arange(0.0, 100.0, 1.0)
        l = matplotlib.pyplot.bar(t1, t1**-2, label = 'LABEL GOES HERE')


        matplotlib.pyplot.title('Voter Graph')
        matplotlib.pyplot.ylabel('Y AXIS LABEL')
        matplotlib.pyplot.xlabel('X AXIS LABEL')
        matplotlib.pyplot.legend()
        matplotlib.pyplot.show()

p1 = plt.bar(ind, dataset[1], width, color='r')
p2 = plt.bar(ind, dataset[2], width, bottom=dataset[1], color='b')
p3 = plt.bar(ind, dataset[3], width, bottom=dataset[2], color='g')
p4 = plt.bar
'''
    #if x == 6:
        #break


#    if x != 1 or 2 or 3 or 4 or 5 or 6:
#        print('Invalid choice. Try again.')
#        break



    #if x is 1, print voter list
    #if x is 2, print out someone's N/S and T/C
    #if x is 3, print out a result

    #random.randint(0,1)
    #if rand == 1:
    #print'north'


#Date time stuff
'''
prints out time when a president wins (after any program is run)
prints out time when a president is confirmed (make the confirmation always 40 days after)
'''
