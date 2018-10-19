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
# # QUESTION:

for i in range(5):
    print("hello world")
    print("there")

for i in range(1, 11):
    print(i)

for i in range(10):
    print(i)

for i in range(2, 100, 3):
    print(i)

for i in range(0, 10, 1):
    print(i)

for i in range(10, 0, -1):
    print(i)

for i in range(3):
    print("a")

a = 0
for i in range(10):
    a = a + 1
print(a)

a = 0
for i in range(10):
    a = a + 1
    for j in range(10):
        a = a + 1
print(a)

i = 0
while i < 10:
    print(i)
    i = i+1

quit = "n"
while quit == "n":
    quit = input("do you want to quit? ")
