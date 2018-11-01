class pizza:
    crust = "regular"
    sauce = "tomato"
    cheese = "mozzarella"
    toppings = ["pepperoni", "mushrooms", "green peppers"]

    def order(self):
        print("the pizza has been ordered")


Noah = pizza()
aaron = pizza()
donal = pizza()
christan = pizza()

"""
print(Noah.crust)
print(Noah.sauce)
print(Noah.cheese)
print(toppings[1])
"""
donal.toppings.append("pineapple")
aaron.crust = "stuffed"

print(Noah.crust)
print(aaron.crust)
print(donal.toppings)
donal.order()


class pizza:
    def __init__(self, crust, sauce, cheese, toppings):
        self.crust = crust
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings

    def __str__(self):
        return (" your crust is: "+str(self.crust)+" your sauce is: "+str(self.sauce)+" your cheese is: "+str(self.cheese)+" your toppings: "+str(self.toppings))


pizza1 = pizza("thin", "red", "fake", "bacon")
print(pizza1)


class Dog:
    def __init__(self, breed, age, name):
        self.age = age
        self.breed = breed
        self.name = name

    def __str__(self):
        return (" your dog's breed is: "+str(self.breed)+" your dog's age is: "+str(self.age)+" your dog's name is: "+str(self.name))


dog1 = Dog("cockapoo", "10", "Betsey")
x = input("what is your dog's name?")
if x == "Betsey":
    print(dog1)

# Assignment


class car:  # car superclass
    def __init__(self, type, age, name, gas):  # things i am setting to car so they can be gained by inheritance
        self.type = type  # everything you are setting for car
        self.age = age
        self.name = name
        self.gas = gas

    def __str__(self):  # this will explain how to print out what is assigned to the car class
        return ("your car type is: "+str(self.type)+" your car's age is: "+str(self.age)+" your car's name is: "+str(self.name)+" your car's gas is: "+str(self.gas))

    def rent(self):  # sets what rent is
        print("this is rented")

    def new(self):  # sets what new is
        print("this is new")


class van(car):  # this will inherit things from car and will have the ability to set things for a van only
    def __init__(self, type, age, name, gas, doors):  # adds doors
        self.type = type
        self.age = age
        self.name = name
        self.gas = gas
        self.doors = doors

    def big(self):  # sets what big is in the van class only
        print("this van is big")

    def __str__(self):  # this is the same as the one in the super class but is edited so that van is printed
        return ("your van type is: "+str(self.type)+" your van's age is: "+str(self.age)+" your van's name is: "+str(self.name)+" your van's gas is: "+str(self.gas)+" your van has this many doors: "+str(self.doors))


class truck(car):  # this will inherit
    def __init__(self, type, age, name, gas, exhaust):
        self.type = type
        self.age = age
        self.name = name
        self.gas = gas
        self.exhaust = exhaust

    def fast(self):
        print("this truck is fast")

    def __str__(self):
        return ("your truck type is: "+str(self.type)+" your truck's age is: "+str(self.age)+" your truck's name is: "+str(self.name)+" your truck's gas is: "+str(self.gas)+" your truck's exhaust size is: "+str(self.exhaust))


car1 = car("cx9", "42", "Mazda", "regular")
print(car1)
car1.rent()
car2 = car("cx5", "0", "Mazda", "regular")
print(car2)
car2.new()
truck1 = truck("dodge", "52", "Ram", "extra", "super big")
print(truck1)
truck1.fast()
van1 = van("compact", "100", "Ford", "premium", "2")
print(van1)
van1.big()
