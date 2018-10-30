#Unit 3 notes

#total sum of all multiples of 3 and 5 until 1000
total_sum = 0
for x in range(1000):
    if (x%3 == 0 or x%5 == 0):
        total_sum = total_sum+x
print (total_sum)

#Python loops below
#For loop
total = 0
for x in range(1,201):
    if x%6 == 0:
        print(x)

#While loop
x=1
while x<201:
    if x%6==0:
        print(x)
    x=x+1

#this will create a random number between 1 and 10
import random
x = random.randint(1,10)

#this will 
import math
try:
    print (math.sqrt(0/0))
except ZeroDivisionError:
    print("can't divide by 0")

x=float(input("Give me a number to divide 7 by"))

#basic try and except, tried something, if it dosent work, except
try:
    print(7/x)
except:
    print ("Can't divide by zero")


def convert_to_celsius(fahrenheit):
    return (fahrenheit-32)*5/9

fahrenheit = float(input("Enter temp in farenheit"))

print(convert_to_celsius(fahrenheit))

#this will ask for three numbers (a,b,c) run it through the math and give you
#how many roots
def how_many_roots(a,b,c):
    d = b**2-4*a*c

    if d<0:
        print("no _roots")
    elif d==0:
        print("one root")
    else:
        print ("two roots")

a = float(input("a?"))
b = float(input("b?"))
c = float(input("c?"))

how_many_roots(a,b,c)
