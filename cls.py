class Myclass:

    # Default constructor with default parameters
    def __init__(self, number=3381, bike="Passion Pro"):
        self.number = number
        self.bike = bike
    
    #parameterized constructor
    # def __init__(self,number,bike):
    #         self.number=number
    #         self.bike=bike 

    # Destructor method (corrected name)
    def __del__(self):
        print("Destructor called...")

p1 = Myclass(7175, "Honda Unicorn")
print(p1.bike)   
print(p1.number) 

p2 = Myclass()
print(p2.bike)   
print(p2.number) 

del p1  
