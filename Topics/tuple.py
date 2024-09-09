# A built-in data type thta lets us create immutable sequences of values
# 
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