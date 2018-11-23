'''Voter Database'''

''' pseudo code

make a dictionary of random first names and last names with two possible locations on a txt document


class president:
    open the dictionary, read it, and print them out
    function that randomizes the first names, last names, and locations per person
    function that defines how many voters in total and then splits the voters in two between 40% and 60% per candidate
    function that will say the names of voters and where they are from (random names + north or south)


Object trump
make trump gets higher percentage of southern voters

object clinton
make clinton gets higher percentage of northern voters

string formatting stuff
make the printed list of every person have upper case names

matplotlib stuff
print out graphs of the amount of people voting for trump or clinton
prints out where the majority of people voted for a specific candidate

datetime stuff
print out time when a president wins
print out time when president is comfirmed (20 days at 12pm)



cd Desktop/Atom/'Computer_Sci.'/'Unit4(b_noah)'/'Business Application Project'

'''
import math
import numpy
import random
import matplotlib
import datetime

f = open('voters.txt', 'r')
voterlist = []
for name in f.readlines():
    voterlist.append([name.split()[0], name.split()[1]])
for name in f.readlines():
    voterlist.append('')
print(voterlist)


class President:
    def __init__(self)
