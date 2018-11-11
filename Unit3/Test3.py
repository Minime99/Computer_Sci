# 1.
for x in range(1, 100+1):
    print(x)
# 2.
for x in range(1, 99+1, 2):
    print(x)
# 3.
for x in range(1, 100+1):
    if x % 4 == 0:
        print(x)
    if x % 5 == 0:
        print(x)
# 4.
for x in range(1, 101):
    if x % 4 == 0:
        print(x)
# 5.
string = str(input("give letters only pls"))
print(string[::2])
# 6.
count = 1
while count <= 100:
    print(count)
    count = count + 1
# 7.
try:
    x = int(input("give a number pls"))
except ValueError:
    print("why not a number?")
else:
    print(x/2)
# 8.


def squarenum(x):
    return x**2


squarenum(4)
# 9.


def wordlength(x):
    return len(x)


wordlength(input("give a word pls"))
# 10.

def difference(x,y):
    return x - y

difference(10,5)
# 11.
def listpro(x):
    p =1
    for i in x:
        p = p*i
    return p

listpro([1,2,3,4,5])
# 12.
def triarea(x,y):
    return (x*y)/2

triarea(10,15)

#class # QUESTION:
