'''Unit 3 Quiz Practice'''

#1
threshold = int(input('Input any natural number'))
for counter in range(1, threshold+1):
    print(counter)

threshold = int(input('Input any natural number'))
counter = 1
while counter<threshold+1:
    print(counter)
    counter = counter+1

try:
    threshold = int(input('Input any natural number'))
except:
    print('You were asked to type a number')
    print('Setting threshold to 10')
    threshold = 10
counter = 1
while counter<threshold+1:
    print(counter)
    counter = counter+1

#2
threshold = int(input('Input any natural number'))
for counter in range(threshold, 0, -1):
    print(counter)

threshold = int(input('Input any natural number'))
while threshold>0:
    print(threshold)
    threshold = threshhold-1

try:
    threshold = int(input('Input any natural number'))
except:
    print('You were asked to type a number')
    print('Setting threshold to 10')
    threshold = 10
finally: #This is not neccessary
    while threshold>0:
        print(threshold)
        threshold = threshold-1



#8
threshold = int(input('Type in a number'))
sum = 0 #Running total, will change as we count up
for x in range(2, threshold, 2): #Counts through even numbers
    sum = sum+x #Adds each number to the total
print(sum)
