dc={"Name":"Piyush","Age":19,"Place":"Kolhapur"}
print(dc)
dict1 = dict([(1, "Apple"), (2, "Banana"), (3, "Mango")])
print("Name",dict1[1])

#Dictionary Functions

dc1={1:"red",2:"black",3:"white"}
print(dc1)
dc1.clear()
print(dc1)

x=("laptop","phone","tab")
y=(12)

dc2=dict.fromkeys(x,y)
print(dc2)

z=dc2.get("laptop")
print(z)

p=dc.items()
print(p)

x1=dc.keys()
print(x1)

dc.pop("Place")
print(dc)


car = {"brand": "Ford","model": "Mustang","year": 1964}
print(car)
car.update({"color": "White"})
print(car)

y=car.values()
print(y)