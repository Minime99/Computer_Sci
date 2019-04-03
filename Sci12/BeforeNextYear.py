class circle():
    def __init__(self,radious):
        self.radious = radious
    def getArea(self):
        return 3.14*self.radious*self.radious
    def getCircumference(self):
        return self.radious*2*3.14

newcircle = circle(12)
print (newcircle.getArea())
print (newcircle.getCircumference())
