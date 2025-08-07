x = {"apple", "banana", "cherry"}
print(x)
y = set(["google", "microsoft", "apple"])
print(y)

n={"rahul","prathmesh","sourit","swarup","aniket"}
for i in n:
    print(i)

print('\n')


#Set Function
x.add("orange")
print(x)

z = x.union(y)
print(z) 

z1=x.intersection(y)
print(z1)

x1={"suresh","vittal","sanjay","anil"}
y1={"pratap","rangrao","shivaji","dadaso"}
x1.update(y1)
print(x1)

print(n)
n.remove("sourit")
print(n)
