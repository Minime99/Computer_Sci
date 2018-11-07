def multi(number1, number2):
    return number1*number2

print(multi(5, 6))

def diff(number1, number2):
    return number1-number2

print(diff(number1=int(input("what is the 1st")), number2=int(input("what is the next?"))))

def sumlist():
    sum=0
    thislist=[1, 2, 3, 4, 5]
    for x in thislist:
        sum=sum + x
    return sum
print(sumlist())

import math

math.factorial(int(input("give a number")))


# or is you want to do it the hard way:

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(int(input("what is your number"))))

def unique_list(L):
  x=[1, 2, 5, 6, 5]
  for a in L:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))
