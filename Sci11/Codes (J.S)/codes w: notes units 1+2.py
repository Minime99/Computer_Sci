("hi")
print("will this text appear")

print ("   ")
thislist = ["apple","banana","cherry"]

for x in thislist:
    print(x)

"""this will print a list of "x" consecutive numbers including zero """
"""in this case 0,1,2,3 because those are 4 digits including 0"""
print ("   ")
for x in range(4):
    print(x)

"""This will create an accesible dictionary where you imput half"""  
print ("   ")
    thisdictionary = {1980:'17%',1981:'15%',1982:'10%'}

x=input("what was the percentage of rain in x year?")
print(thisdictionary[x])

"""this will print a list of whats in the [ ] with with a break at a term"""
fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

"this will create a list of numbers less than 6"
i = 1
while i < 6:
    print(i)
    i+=1

"this will create a list of numbers in order going on forever"
"starting at 1"
i = 1
while 1 < 6:
    print(i)
    i+=1

"""this will create a loop where you can input"""
"""any number you want, and if its not 10 it will loop back to the question"""
x = 1
while (x != 10):
    x = int(input("say a number."))

"""this will create a random number between from 1-10"""
import random 
print(random.randint(1,10))

"""this will create a response if the dice match or not"""
"this will create a pair of random numbers between 1-6 or dice"
"that will randomize at the same time"
"this would also work if you just replaced the named dice with print"""
import random

""" "while(True):" with the "break" after the "Match. Yay"
"will loop the dice until there is a match
can add a many operations of dice as needed"""
while(True):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)

    print(dice1)
    print(dice2)
    print(dice3)
    
    if dice1 != dice2 != dice3:
        print("No match. No fun")
        
    if dice1 == dice2 == dice3:
        print("Match. Yay")
        break

    
food = 'spam'

if food == 'spam':
    print('Ummmm, my favorite!')
    print('I feel like saying it 100 times...')
    print(200 * (food + '! '))
    
    
x=7
y=7.0

if x < y:
    print('x is smaller')
elif x > y:
    print('x is larger')
else:
    print('invalid choice')
    
choice = input('What do you choose?')

if choice == 'a':
    print("You chose 'a'.")
elif choice == 'b':
    print("You chose 'b'.")
elif choice == 'c':
    print("You chose 'c'.")
else:
    print("Invalid choice.")
    
print ("   ")
thislist = ["a","b","c","b again"]

print (len(thislist))

thistuple = ("a", "b", "c","d")
print(len(thistuple))

thisset = {"a", "b", "c","d"}

for x in thisset:
  print(x)
  
index =	{
  "A": "b",
  "B": "c",
  "Car": "FAST"
}
print(index)
        



