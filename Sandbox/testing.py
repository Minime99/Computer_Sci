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
