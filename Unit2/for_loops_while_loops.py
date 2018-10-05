# For loops” execute the indented code as many times as the loop is told to.
# ●	If passed a list, it will go through the list, item by item.
# ●	If passed a range of numbers, it will go through them, one by one.
# ●	If passed a string, it will go through it character by character.


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

# putting break in will make it end at "banana" so only apple will be printed
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

# 0-62
for x in range(62):
    print(x)
# 2-30 by 3
for x in range(2, 30, 3):
    print(x)

# “while loops” execute the indented code as long as the conditional statement is true.
i = 1
while i < 6:
    print(i)
    i = i+1

x = 1
while (x != 10):
    x = int(input("say a number"))
# first look at random logic need to import as without it python will not know what random is
import random

print(random.randint(1, 10))
