''' Day 1       November 14'''

#To find a file and use it somewhere
#Type 'ls' in terminal
#Type the folder by typing 'cd' then folder
#When you find the file, type    python3 'name of file'
#Must be .py file
#'r' means read, 'w' means write, 'a' means append a str to end of .txt file

f = open('sampletext.txt', 'r')
x = f.readlines()
for line in x:
    print('Line! :',line)
    print(line.replace(',no','ABSOLUTELY NOT'))
    print(line.split(' ')[1].split(':'))



'''Day 2       November 15'''

print('Script Starting')
f = open('sampletext.txt', 'r+w+a')
f.readlines()
f.write('This line is added to the file')
f.append(str(x))
print('Script Ending')

#to remove files from os permanently
import os
try:
    os.remove('sampletext.txt')
except OSError:
    print('Can not find file')

#Deleting folders
import os
try:
    os.remove('Faketext.txt')
except OSError:
    print('Can not find file')
for x in os.listdir('Folder to remove'):
    os.remove('Folder to remove'+g)
os.rmdir('Folder to remove')

f = open('sampletext.txt', 'w')
for x in range(0,10):
    f.write(str(x))
    f.write('\n')


'''Day 3        November 19'''

#To make a new text file:                           x = open('name of new file.txt', 'w')
#To open a text file in the following modes:        x = open('already exiting file.txt', 'r+a+w')
#Read a text file and make string manipulations:    text = x.read()
#Convert things in a text file:                     x = text.upper()    x = text.upper()    x = text.count('a') x = text.replace('a','$')
#Write in a newly created text file:                x.write('The file will contain this')   In 'w' mode
#Append the end of a text text file:                x.write('this is added to the end')     In 'a' mode
#Close the document                                 x.close()
#This line is a comment

f = open('surprisedpikachu.txt', 'w')
f.close()
f = open('surprisedpikachu.txt', 'a')
f.write('this aint it chief')
f.close()
f = open('surprisedpikachu.txt', 'r')
text = f.read()
f.close()
f = open('text999.txt', 'w')
newtext = text.replace('s', '$')
f.write(newtext)
f.close()


'''Day 4        November 22'''

import matplotlib.pyplot
matplotlib.pyplot.plot([1,2,3,4])
matplotlib.pyplot.ylabel('some numbers')
matplotlib.pyplot.show()

import numpy
import matplotlib.pyplot
x = numpy.arange(0, 5, 0.1)
y = numpy.sin(x)
matplotlib.pyplot.plot(x, y)
matplotlib.pyplot.show()

import matplotlib.pyplot
import numpy                                        # similar to the math module
def f(t):
    s1 = numpy.cos(2 * numpy.pi * t)
    e1 = numpy.exp(-t)
    return s1 * e1
t1 = numpy.arange(0.0, 5.0, .2)
l = matplotlib.pyplot.plot(t1, f(t1), 'ro')
matplotlib.pyplot.setp(l, markersize=10)
matplotlib.pyplot.setp(l, markerfacecolor='red')
matplotlib.pyplot.show()

import matplotlib.pyplot
import style
import math
x=[]
y=[]
for i in range(360):
    x.append(i)
for j in range(360):
    y.append(math.cos(j*3.1415/180))
pyplot.plot(x,y, label='y=cos(x)')
pyplot.title('Cosine graph')
pyplot.ylabel('y value')
pyplot.xlabel('x value')
pyplot.legend()
pyplot.show()
