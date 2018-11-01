import random
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def pricing(self):
        if car1>30000:
            print('This is kinda pricey. I will still buy it though because it is such a cool car.')
        if car1<25000:
            print('Wow great price! Definetely gonna buy this!')
        if car2>30000:
            print('This is kinda pricey. I will still buy it though because it is such a cool car.')
        if car2<25000:
            print('Wow great price! Definetely gonna buy this!')
    def rev(self):
        print('VROOOOOM!')

class Car1(Car):
    def __init__(self, make, model, year):
        self.make = 'Ford'
        self.model = 'Mustang'
        self.year = 1967
    def pricing(self):
        car1 = random.randint(20000, 36000)*1000
        if car1>30000:
            print('This is kinda pricey. I will still buy it though because it is such a cool car.')
        if car1<25000:
            print('Wow great price! Definetely gonna buy this!')
    def rev(self):
            print('VROOOOOM')

class Car2(Car):
    def __init__(self, make, model, year):
        self.make = 'Chevrolet'
        self.model = 'Camaro'
        self.year = 1971
    def pricing(self):
        car2 = random.randint(20000, 36000)*1000
        if car2>30000:
            print('This is kinda pricey. I will still buy it though because it is such a cool car.')
        if car2<25000:
            print('Wow great price! Definetely gonna buy this!')
    def rev(self):
        print('VROOOOOM')

question = input('What car would you like to know about?')
if question == 'Mustang':
    print(Car1)
if question == 'Camaro':
    print(Car2)
