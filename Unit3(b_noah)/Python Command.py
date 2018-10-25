def how_many_roots(a,b,c):
    d = b**2-4*a*c              #D=b^2-4ac      discriminate is part of quadratic formula
    if d<0:                     #if D is negative - No roots
        print('No roots')
    elif d==0:                  #if D is 0 - One root
        print('One root')
    else:                       #if D is positive - Two roots
        print('Two roots')
a = float(input('a?'))
b = float(input('b?'))
c = float(input('c?'))
how_many_roots(a,b,c)

def square_this(x):
    return x**2
number = int(input('What do you want to square?'))
print(square_this(number))
