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
    def __init__(self):
        self.crust = "regular"
        self.sauce = "tomato"
        self.cheese = "mozzarella"
        self.toppings = ["pepperoni", "mushrooms", "green peppers"]

    def order(self):
        print("the pizza has been ordered")


noah = pizza()
print(noah.crust)


class Dog:
    def __init__(self):
        self.age = 0
        self.breed = "unkown"
        self.shots = ["rabies", "lepto", "cancer"]

    def __str__(self):
        return(self.breed+" "+str(self.age))


Betsey = Dog()
