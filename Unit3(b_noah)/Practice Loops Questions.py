'''Day 1'''
numbers = []
for x in range(200):
    if x%6 == 0:
        print(x)

'''Day 2'''
for i in range(5):
    print('Hello')
print('There')

for i in range(5):
    print('Hello')
    print('There')


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
    print('a')
for j in range(3):
    print('b')


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

a = 0
for i in range(10):
    a = a + 1
    for j in range(10):
        a = a + 1
print(a)


for i in range(1,5):
    for j in range(11,15):
        print('i is',i,'and j is',j)


i = 0
while i < 10:
    print(i)
    i = i + 1


quit = 'n'
while quit == 'n':
    quit = input('Do you want to quit')
