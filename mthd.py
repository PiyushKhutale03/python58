# Example of method overriding in Python
class A:
    def func1(self):
        print("func1 from class A")
    def func2(self):
        print("func2 from class A")
    
class B(A):
    def func1(self):
        print("func1 from class B")
    def func2(self):
        print("func2 from class B")
        
b=B()
b.func1()
b.func2()

# Example of method overloading 
def add(datatype, *args):
    if datatype == 'int':
        answer = 0
    if datatype == 'str':
        answer = ""

    for i in args:
        answer += i

    print(answer)

add('int', 5, 6)       
add('str', "Hello ", "World")  
                                                                                                                        