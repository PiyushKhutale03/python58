class mynum:
    num = 58                   # Public variable
    _protected_var = "Hello"   # Protected variable 
    __private_var = "Piyush"   # Private variable 

    def __init__(self):
        self.num = 58
        self._protected_var = "Hello"
        self.__private_var = "Piyush"

    def get_private(self):
        # Access private variable inside the class
        return self.__private_var

    def get_protected(self):
        # Access protected variable inside the class
        return self._protected_var
    
obj = mynum()

print(obj.num)
print(obj._protected_var)     

print(obj.__private_var)    # Error!

print(obj.get_private())      

 