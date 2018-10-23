# place to try out new or random code
"""Operation	What it returns

   x + y	        Sum of x and y
   x - y	        Difference of x and y
   -x	            Changed sign of x
   +x	            Identity of x
   x * y	        Product of x and y
   x / y	        Quotient of x and y
   x // y	        Quotient from floor division of x and y
   x % y	        Remainder of x / y
   x ** y	        x to the y power
"""
FirstInt = input("Number1")
SecondInt = input("Number2")
Result = int(FirstInt) + int(SecondInt)
print("The result is:", Result)

if Result == 10:
    print("Yes")

import random

while (True):
    card1 = (random.randint(1, 50))
    card2 = (random.randint(1, 50))

    print(card1)
    print(card2)

    if card1 == card2:
        print("Same")
        break

# basic caculator


def add(num1, num2):
    return num1+num2


def subtract(num1, num2):
    return num1-num2


def multiply(num1, num2):
    return num1*num2


def divide(num1, num2):
    return num1/num2


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("enter 1,2,3,4")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")

# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

# To take coefficient input from the users
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The solutions are {0} and {1}'.format(sol1, sol2))

try:
    x = int(input("give me a number between 1 and 7"))
    print(x + 1)
except ValueError:
    print("this is not a number")

age = int(input("how old are you?"))
name = input("what is your name?")
year = str((2018-age)+100)
print(name + "you will be 100 in the year" + year)
total = 0

num = int(input("give me a number"))
repeat = num
product = sum(num*10**n for n in range(repeat))
print(product)

'''Connect 4 Game'''


print('You win!')
