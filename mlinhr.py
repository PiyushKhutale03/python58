class Person:
    def __init__(self, name):
        self.name = name

class Team(Person):
    def __init__(self, name):
        super().__init__(name) 

    def show_rule(self):
        print(self.name, "is a Batsman")


class Cricketer(Team):
    def __init__(self, name):
        super().__init__(name)  

    def department(self, dept):
        print(self.name, "is playing for team", dept)


d = Cricketer("Rohit Sharma")
d.show_rule()
d.department("Mumbai Indians")
