x = int(input("put in number"))  # int turns the str into an integer so it works with < and >

if x < 10:
    print("smaller")
elif x > 10:
    print("larger")

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

# strings
"""
x = "abcdefg"
x[1] gives "b"
x[2:5] gives "cde"
len(x) gives 7
x.upper() gives "ABCDEFG"
x.replace("a", "9") gives "9bcdefg"
"""
# lists
"""
x = ["apples","bananas","carrots"]
x[1] is "bananas" as apples is really 0 in the list
tuples
set
dictionaries
"""
# # REVIEW:

# 1.
x = str(12)
y = str(13)
print(x + y)
# 2.
x = int(input("first number"))
y = int(input("other number"))
print(x+y)
# 3.
x = input("lower letter")
print(x.upper())
# 4.
x = ["apples", "bananas", "carrots", "gun"]
print(x)
x.remove("carrots")
print(x)
# 5.
x = {"apples": 8, "bananas": 10}
print(x)
x.update({"guns": 4})
print(x)
# 6.
x = input("8 letters pls")
if len(x) < 8:
    print("nope")
elif len(x) == 8:
    print("thx")
# 7.
x = set([1, 2, 3, 4])
print(x)
print(len(x))
# 8.
x = input("10 letters pls")
print(x)
print(x[3:6])
# 9.
x = input("10 letters pls")
print(x)
print(x[5:10])  # needs something else
