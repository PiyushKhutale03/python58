import array as arr
a = arr.array('i', [1, 1, 2, 2, 2, 2, 23])
print(*a)

#Accessing an element
b = arr.array('d', [2.5, 3.2, 3.3])
print(b[1])
print(b[2])

#Array Functions

#1.insert()
a.insert(1, 4)  # Insert 4 at index 1
print(*a)

#2.remove()
a.remove(1)
print(a)

#3.pop()
a.pop(2)
print(a)

#4.index()
print(a.index(2))

#5.count()
count = a.count(2)
print(count)

#6.reverse()
b.reverse()
print(*b)

#7.extend()
a.extend([6,7,8,9,10])
print(a)

#8.sort()
a = arr.array('i', sorted(a))
print(*a)

#9.append()
a.append(84)
print(a)

#10.clear()
b.clear()
print(b)