import random

x = random.randint(1, 10)
print(x)

# # HACK:
import random

while(True):
    dice1 = (random.randint(1, 6))
    dice2 = (random.randint(1, 6))

    print(dice1)
    print(dice2)

    if dice1 == 6:
        if dice2 == 6:
            print("done")
            break
# or
import random
x = random.randint(1, 6)
while x != 6:
    x = random.randint(1, 6)
    print(x)

import random
randnum = (random.randint(1, 48))
while(True):

    guess = int(input("what is the number (1-48)"))

    if guess == randnum:
        print("you got it!")
        break
