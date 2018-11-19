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
