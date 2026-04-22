# A built-in data type that lets us create immutable sequences of values

tup = (2,3,4,5)
print(type(tup))
print(tup[1:3]) #slicing
print(tup[0])
print(tup[1])

tup = (2)
print(type(tup))

tup = (4,)
print(type(tup))

#turple methods

tup1 = (2,1,3,1)
print(tup1.index(1)) #returns index of first occurence
print(tup1.count(1)) #counts total occurences
print(tup1)

#nested tuples
nested_tuple = ("data",(1,2,3),[4,5,6])
print(nested_tuple)
print(type(nested_tuple))

#mixed datatypes
my_tuple = (1, "hello", 3.14, (1,2,3))
print(type(my_tuple))

#tuple constructor
a = tuple(("a","b","c"))
print(a)
print(type(a))

# converting to list
b=(25,26,27,28,29)
c=list(b)
c.remove(27)
u=tuple(c)
print(u)


# loop
thistuple = ("a","b","c")
for x in thistuple:
    print(x)

# join 2 tuple
tuple1 = ("a","b","c")
tuple2 = (1,2,3)
tuple3 = tuple1 + tuple2
print(tuple3)

# multiply tuple
my_tuple = ("hello",) * 3
print(my_tuple)