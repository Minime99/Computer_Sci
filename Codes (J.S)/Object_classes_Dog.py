class Dog:
    def __init__(sel, age, breed, name):
        self.age = age
        self.breed = breed
        self.name = name

    def ruff(self):
        print("Ruff!")

class cockapoo(Dog):
  def __init__(self,age,breed,name):
      Dog.__init__(self,age,breed,name)

      def besmart(self):
          print("E equals m c squared")

dog1 = cockapoo(10,"cockapoo","Lola")
dog1.ruff()
dog1.beSmart()

dog2 = Dog(8,"Mastiff","Xena")
dog2.ruff()
#dog2.beSmart()
