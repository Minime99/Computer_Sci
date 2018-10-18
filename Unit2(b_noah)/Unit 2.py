'''Day 1'''

thislist = ['apple', 'banana', 'cherry', 'durian', 'eggplant', 'strawberry', 'pear', 'kiwi']
print(len(thislist))
for x in thislist:
    print(x)


'''Day 2'''

fruit = ['apple', 'banana', 'cherry', 'strawberry']
for x in "banana":
    print(x)


fruit = ['apple', 'banana', 'cherry', 'strawberry']
for x in fruit:
    if x == 'banana':
        break
    print(x)


for x in range(6090):
    print(x)


for x in range(2, 30, 3):
    print(x)
i = 1
while i < 6:
    print(i)
    i = i+1


x = 1
while (x != 10):
    x = int(input('Say a number. '))


import random
print(random.randint(1,10))


import random
print(random.randint(1,6))
print(random.randint(1,6))


import random
while(True):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(dice1)
    print(dice2)
    if dice1 != dice2:
        print('Sucks. Try again bro.')
    if dice1 == dice2:
        print('Congratulations! You have doubles!')
        break


'''Day 3'''

inputnumber = input("What is the number?")
# Break the number apart into digits
# Input already gives you a string
outputnumber = ''
for c in inputnumber:
    # c sqaured is
    s = int(c)**2
    outputnumber = outputnumber + str(s)
# Square every digit
# Ram those answers together into one answer
# Output the answer
print(outputnumber)


'''Day 4 (Wed Oct 10)'''

food = 'spam' #variable is <type:'str'>
if food == 'spam':
    print('Ummmm, my favorite!')
    print('I feel like saying it 100 times...')
    print(100 * (food + '! '))


food = 'spam'
if food == 'spam':
    print('Ummmm, my favorite!')
else:
    print("No, I won't have it. I want spam!")


food = 'deep fried cabbage lasagna'
if food == 'spam':
    print('Ummmm, my favorite!')
else:
    print("No, I won't have it. I want spam!")


x=8
y=7
if x < y:
    print('x is smaller than y.')
elif x > y:
    print('x is greater than y.')
else:
    print('x is neither smaller nor larger.')


choice = input('What do you choose?')
if choice == 'a':
    print("You chose 'a'.")
elif choice == 'b':
    print("You chose 'b'.")
elif choice == 'c':
    print("You chose 'c'.")
else:
    print("Invalid choice.")


x = 60
if 1 < x:            # assume x is an int here
    print('x is smaller.')
    if x < 10:
        print("x is a positive single digit.")



x = input ('Pick a number')
x = int(x) #Casting the variable from string to int
if x<10:
    print('smaller')
elif x>10:
    print('larger')
else:
    print('equal')
