class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)

class Male(Person):
    def task(self):
        print(self.firstname,"is a male.")

d=Male("Son","Goku")
d.printname()
d.task()