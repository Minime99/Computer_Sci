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
