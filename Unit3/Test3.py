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
        if x % 5 == 0:
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


def difference(x, y):
    return x - y


difference(10, 5)
# 11.


def listpro(x):
    p = 1
    for i in x:
        p = p*i
    return p


listpro([1, 2, 3, 4, 5])
# 12.


def triarea(x, y):
    return (x*y)/2


triarea(10, 15)

# class # QUESTION: # this is an advanced class question and most likly will be different on the test


class contact:
    def __init__(self, name, age, school, id):
        self.name = name
        self.age = age
        self.school = school
        self.id = id

    def __str__(self):
        return("your name is:"+str(self.name)+"your age is:"+str(self.age)+"your school is:"+str(self.school)+"your id is:"+str(self.id))

    def friend(self):
        print("this is a friend")


class contact1(contact):
    def __init__(self, name, age, school, id, col):
        self.name = name
        self.age = age
        self.school = school
        self.id = id
        self.col = col

    def __str__(self):
        return("your name is:"+str(self.name)+"your age is:"+str(self.age)+"your school is:"+str(self.school)+"your id is:"+str(self.id)+"yourfillis:"+str(self.col))


person = contact("jill", "43", "mentor", "1234")
print(person)
person.friend()

noah = contact1("noah", "1", "2", "4", "3")
print(noah)


# # REVIEW:

numbers = [1, 10, 20, 30, 40, 50]
sum = 0
for number in numbers:
    sum = sum+number

print(sum)

numbers = [1, 10, 20, 30, 40, 50]
sum = 0
for x in numbers:
    sum = x

print(sum)  # is not the same as above as it will not add anythin and just go throught the list

a = 0
while a < 10+1:
    print(a)
    a = a + 1  # will print out numbers 1 to 10 as you are adding 1 to 10


def getkids():  # defines a method to be used later, no paramaters as they are passed to a function
    try:  # python trys to do this code
        x = int(input("how many kids do you have?"))
    except:  # if there was any error
        return "yer wot?"
    else:
        return(x)  # gets sent back to whenever the function was called
    finally:
        print("T time")
    return x


print(getkids())  # print out anything that is returned by the function getkids()

PI = 3.14


def circleArea(radius):  # 5 is passed into this function
    return PI*radius*radius  # it is used in here


print("circle area with radious 5: ")
print(circleArea(5))  # runs the function with 5


class Cal(object):  # a template of methods and attributes
    pi = 3.142

    def __init__(self, radius):  # methods
        self.radius = radius  # attributes

    def area(self):
        return self.pi * (self.radius ** 2)


a = Cal(32)
print(a.area())
