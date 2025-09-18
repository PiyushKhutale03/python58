class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

class Colour:
    def __init__(self, colour):
        self.colour = colour
        super().__init__()  

class Car(Vehicle, Colour):
    def __init__(self, wheels, colour):
        super().__init__(wheels) 
        self.colour = colour  

    def details(self):
        print(self.wheels, "wheeler is a car of colour", self.colour)


audi = Car("4", "Black")
audi.details()
