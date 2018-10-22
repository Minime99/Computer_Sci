'''Day 1    Oct 17'''

total = 0
for x in range(2001):
    total = total + x
print(total)

x = 10
for x in range(2, 6):
    print(x)

for x in range(1, 11):
    print(x, 'Ahoy!')

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

for x in range(1,11):
    for y in range(1,11):
        print(x, 'times', y, 'is', x*y)

total = 0
for x in range(1000):
    if x%3 == 0:
        total = total + x
    elif x%5 == 0:
        total = total + x
        print(total)
print(total)

numbers = []
for x in range(1000):
    if x%3 == 0 or x%5 == 0:
        print(x)


'''Day 2'''

#For Loop
for x in range(1,201):
    if x%6 == 0:
        print(x)
#The For and While Loop are equivalent
#While Loop
x = 1
while x<201:
    if x%6 == 0:
        print(x)
    x=x+1

#Dice Rolling
import random               #Add a random number capability
x=random.randint(1,6)       #Random number between 1 and 6
#if x!=6:
#    repeat roll            #This is the pseudo code version
while x!=6:
    x=random.randint(1,6)
    print(x)

import random
magicnumber=random.randint(1,10)
x=input('Guess my magic number')
while x!=magicnumber:
    print('Nope. Try again!')
    break
if x==magicnumber:
    print('Wow that was a good guess!')
    break
break


'''Day 3'''

#Try and Except
x = input('What is your favorite number?')
print('You chose', x)
x = int(x)
try:
    print('Half of it is',x/2)                  #Cannot take half a str
except TypeError:
    print('Type a number, fool')

#We need to import 'math' to do square roots
import math
print(math.sqrt(64))

import math
try:
    print(math.sqrt(0/0))
except ZeroDivisionError:
    print("Can't divide by zero")
