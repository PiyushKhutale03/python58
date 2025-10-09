class Emp:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class fun(Emp):
    def __init__(self, id, name, email):
        super().__init__(id, name) 
        self.email = email

obj = fun(101, "Rangrao", "Rangrao@email.com")
print(obj.id, obj.name, obj.email)