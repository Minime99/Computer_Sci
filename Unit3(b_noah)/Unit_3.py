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

for x in range(1, 11):
    for y in range(1, 11):
        print(x, 'times', y, 'is', x*y)

total = 0
for x in range(1000):
    if x % 3 == 0:
        total = total + x
    elif x % 5 == 0:
        total = total + x
        print(total)
print(total)

numbers = []
for x in range(1000):
    if x % 3 == 0 or x % 5 == 0:
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
#Try, Except, and Finally

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

try:
    x=float(input('Give me a number to divide 7 by'))
    print(7/x)
except ZeroDivisionError:
    print("Can't divide by 0")
except ValueError:
    print("Can't divide by a string")
finally:                                          #Runs no matter what
    print('Program over')

x = float(input('Give me a positive number'))
if x < 0:
    raise Exception('Sorry, no numbers below zero') #What the user sees


'''Day 4'''
#def and return
def my_function():
    print('Hello from inside my function')
my_function()

def double_it(x):
    return 2 * x
print(double_it(3))
print(double_it(5))
print(double_it(9))

def my_function(first_name):
    print(first_name + ' should probably have a last name too')
my_function('Emil')
my_function('Tobias')
my_function('Linus')

def convert_to_celsius(fahrenheit):
    return (fahrenheit-32)*5/9
fahrenheit = float(input('Enter temp in fahrenheit'))
print(convert_to_celsius(fahrenheit))

def convert_to_celsius(fahrenheit):
    return (fahrenheit-32)*5/9
for x in range(30,50,2):
    print(x, 'fahrenheit is', convert_to_celsius(x), 'C')


'''Day 5'''

#Unofficial but easier way to do it
class Pizza:
    crust = 'regular'
    sauce = 'tomato'
    cheese = 'mozzarella'
    toppings = ['pepperoni', 'bacon', 'meatballs']
    def order(self):
        print('The pizza has been ordered')

class Pizza:
    crust = 'regular'
    sauce = 'tomato'
    cheese = 'mozzarella'
    toppings = ['pepperoni', 'bacon', 'meatballs']
    def order(self):
        print('The pizza has been ordered')
noahs_standard_pizza = Pizza()
noahs_favorite_pizza = Pizza()
noahs_favorite_pizza.crust = 'stuffed crust'
noahs_favorite_pizza.toppings.append('extra cheese')

#Official Way to do it
class Pizza:
    def __init__(self):             #Double underscore means 'Run this code each time an object is made'
        self.crust = 'regular'
        self.sauce = 'tomato'
        self.cheese = 'mozzarella'
        self.toppings = ['pepperoni', 'bacon', 'meatballs']
    def order(self):
        print('The pizza has been ordered')

class Dog:
    def __init__(self):
        self.breed = 'Samoyede'
        self.age = 7
    def order(self):
        print('This is your dog')
luna = Dog()
tundra = Dog()
tundra.breed = 'Husky'
tundra.age = 12
print('Luna is a', luna.breed, 'and is', luna.age, 'years old.')
print('Tundra is a', tundra.breed, 'and is', tundra.age, 'years old.')
