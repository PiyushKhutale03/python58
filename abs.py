from abc import ABC, abstractmethod
class Abs(ABC):
    @abstractmethod
    def do_something(self):
        pass
    
class impl(Abs):
    def do_something(self):
        return "Working..."

i=impl()
print(i.do_something())