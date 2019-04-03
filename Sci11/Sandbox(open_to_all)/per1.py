class vehicle:
    def __init__(self, name, kind, color, value):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = 100
        def description(self):
            desc_str = "this is a" + " " + self.name + " " + "and it is worth" + " " + str(self.value) + " " + "it is also" + " " + self.color
            return desc_str

car1 = vehicle("name", "fer", "blue", 1000000)
description()
