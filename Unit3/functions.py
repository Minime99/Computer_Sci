def my_function():
    print("hello from inside the function")


my_function()

# return values


def dounble_it(x):
    return 2*x


print(dounble_it(2))
print(dounble_it(5))
print(dounble_it(9))
# (32°F − 32) × 5/9 = 0°C


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


fahrenheit = int(input("enter temp in f"))

print(convert_to_celsius(fahrenheit))


def how_many_roots(a, b, c):
    d = b**2-4*a*c
    if d > 0:
        print("there are no roots")
    elif d == 0:
        print("there is one root")
    else:
        print("two roots")
    return d


a = float(input("a"))
b = float(input("b"))
c = float(input("c"))

how_many_roots(a, b, c)
