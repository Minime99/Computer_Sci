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

numbes = []
for x in range(1000):
    if x % 3 == 0 or x % 5 == 0:
        print(x)
