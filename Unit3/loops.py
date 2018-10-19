# puts numbers from 0 to 5 not 0 to 6
for x in range(6):
    print(x)

total = 0
for x in range(2001):
    total = total+x
print(total)

for x in range(2, 6):
    print(x)

for x in range(1, 11):
    print(x, "ahoy!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

for x in range(1, 6):
    for y in range(1, 6):
        print(x, "times", y, "is", x*y)
total = 0
for x in range(1, 1001):
    if x % 3 == 0:
        total = total+x
    elif x % 5 == 0:
        total = total+x
print(total)

# # NOTE:
# for loop
total = 0
for x in range(1, 201):
    if x % 6 == 0:
        print(x)
# while loop
x = 1
while x < 201:  # as long as this is true
    if x % 6 == 0:
        print(x)
    x = x+1
