import random

while(True):
    dice1 = (random.randint(1, 6))
    dice2 = (random.randint(1, 6))

    print(dice1)
    print(dice2)

    if dice1 == dice2:

        print("you win")
        break
