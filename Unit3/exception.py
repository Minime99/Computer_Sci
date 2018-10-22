x = input("what is your favorite number?")
print("you chose", x)


# # REVIEW:
try:
    x = int(input("what is your favorite number?"))
    print("you chose", x)
    print("half of it is", x/2)  # cant take half of str
except ValueError:
    print(':( type a number pls')

import math

try:
    print(math.sqrt(0/0))
except ZeroDivisionError:
    print("you cant / by 0")

import math
x = float(input("give me a number to divide by 7"))
try:
    print(7/x)
except:
    print("cant divide by 0")
finally:  # runs no matter what
    print("program over")
