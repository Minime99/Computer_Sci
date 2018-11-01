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
        self.type = type  # everything you var. are setting for car superclass
        self.age = age
        self.name = name
        self.gas = gas

    def __str__(self):  # this will explain how to print out what is assigned to the car class
        return ("your car type is: "+str(self.type)+" your car's age is: "+str(self.age)+" your car's name is: "+str(self.name)+" your car's gas is: "+str(self.gas))

    def rent(self):  # sets what rent is
        print("this is rented")

    def new(self):  # sets what new is
        print("this is new")


class van(car):  # this will inherit things from the superclass car and will have the ability to set things for the van subclass only
    def __init__(self, type, age, name, gas, doors):  # adds doors
        self.type = type
        self.age = age
        self.name = name
        self.gas = gas
        self.doors = doors  # doors var. set for van only

    def big(self):  # sets what big is in the van subclass only
        print("this van is big")

    def __str__(self):  # this is the same as the one in the super class but is edited so that van is printed
        return ("your van type is: "+str(self.type)+" your van's age is: "+str(self.age)+" your van's name is: "+str(self.name)+" your van's gas is: "+str(self.gas)+" your van has this many doors: "+str(self.doors))


class truck(car):  # this will inherit things from the superclass car and will be seperate from the van subclass as well as be able to set new things for the truck subclass only
    def __init__(self, type, age, name, gas, exhaust):
        self.type = type
        self.age = age
        self.name = name
        self.gas = gas
        self.exhaust = exhaust  # exhaust var. set for truck only

    def fast(self):  # sets what fast is for truck only
        print("this truck is fast")

    def __str__(self):  # this is the same as the one in the superclass just edited so that it says truck instead
        return ("your truck type is: "+str(self.type)+" your truck's age is: "+str(self.age)+" your truck's name is: "+str(self.name)+" your truck's gas is: "+str(self.gas)+" your truck's exhaust size is: "+str(self.exhaust))


# sets what type,age,name,and gas car1 is from the car superclass
car1 = car("cx9", "42", "Mazda", "regular")
print(car1)  # after setting what car1 is using the car class prints it out
car1.rent()  # runs what rent is from the car superclass
# sets what type,age,name,and gas car2 is from the car superclass
car2 = car("cx5", "0", "Mazda", "regular")
print(car2)  # after setting what car1 is using the car class prints it out
car2.new()  # runs what new is from the car superclass
# sets what type,age,name,gas, and exhaust truck1 is from the truck subclass
truck1 = truck("dodge", "52", "Ram", "extra", "super big")
print(truck1)  # after setting what truck1 is using the car class prints it out
truck1.fast()  # runs what fast is from the truck subclass
# sets what type,age,name,gas, and doors van1 is from the van subclass
van1 = van("compact", "100", "Ford", "premium", "2")
print(van1)  # after setting what van1 is using the car class prints it out
van1.big()  # runs what big is from the van subclass

# proves that the superclass is connceted to car1,car2,truck1,and van1
print('car1 is a car?', isinstance(car1, car))
# also proves that the subclasses are seperate from the superclass
print('car2 is a car?', isinstance(car2, car))
print('truck1 is a truck?', isinstance(truck1, truck))
print('truck1 is a car?', isinstance(truck1, car))
print('car1 is a truck?', isinstance(car1, truck))
print('car2 is a truck?', isinstance(car2, truck))
print('van1 is a truck?', isinstance(van1, truck))
print('van1 is a van?', isinstance(van1, van))
print('van1 is a car?', isinstance(van1, car))
print('car1 is a van?', isinstance(car1, van))
print('car2 is a van?', isinstance(car2, van))
