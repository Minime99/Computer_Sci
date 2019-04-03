#This is my superclass because there are many types of Ice cream
class Ice_cream:
#Declaring my instance variables
    def __init__(self,texture,flavour,colour):
        self.texture = texture
        self.flavour = flavour
        self.colour = colour
#Declaring instance method 1
    def lick(self):
            print("The Ice cream was licked!")
#Declaring instance method 2
    def beTasty(self):
         print("The ice cream is tasty")
#This is my first subclass which will inherit the same properties as Ice cream
class strawberry(Ice_cream):
  def __init__(self,texture,flavour,colour):
      Ice_cream.__init__(self,texture,flavour,colour)
#This is my second subclass which will inherit the same properties as Ice cream
class vanilla(Ice_cream):
  def __init__(self,texture,flavour,colour):
      Ice_cream.__init__(self,texture,flavour,colour)

#Creating objects of subclass 1
Ice_cream1 = strawberry("smooth","strawberry","pink")
Ice_cream1.lick()
Ice_cream1.beTasty()
#creating objects of subclass 2
Ice_cream2 = vanilla("sweet","vanilla","white")
Ice_cream2.lick()
Ice_cream2.beTasty()
#Code that demonstrates that my superclass object is only an instance of
#my superclass
print('Ice_cream is strawberry?', isinstance(Ice_cream,strawberry))
print('Ice_cream is vanilla?', isinstance(Ice_cream,vanilla))
#Code that demonstrates that my subclass's object is only an instance of
#my subclass's
print('Ice_cream1 is strawberry?', isinstance(Ice_cream1,strawberry))
print('Ice_cream1 is vanilla?', isinstance(Ice_cream1,vanilla))
print('Ice_cream2 is strawberry?', isinstance(Ice_cream2,strawberry))
print('Ice_cream2 is smooth?', isinstance(Ice_cream2,vanilla))
print("Intel Core")
