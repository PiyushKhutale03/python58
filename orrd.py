
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Sher(Animal):
    def sound(self): 
        print("Sher dhaad!!!!")

a = Animal()
d = Sher()

a.sound()  
d.sound()
