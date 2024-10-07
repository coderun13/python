# Set is the collection of the unordered items(no index).
# Each element in the set must be unique and immutable.
# Set is mutable but not elements.
# We can't store list and dict in set.
# It ignore duplicate values

collection = {1,2,3,4,5,2,"hello","snehal"}

print(collection)
print(type(collection))
print(len(collection)) #ignores duplicate items

# empty set
new = set()
print(new)
print(type(new))

# Set Methods
# set.add(el) -> add an element
# set.remove(el) -> removes the element
# set.clear() -> empties the set
# set.pop() -> removes a random value
# set.union(set2) -> combines both set values and returns new
# set.intersection(set2) -> combines common values and return new

new.add(8)
new.add(2)
new.add(2)
new.add(3)
new.add(4)
new.add(5)
print(new)

new.remove(3)
print(new)

# new.clear()
# print(new)

print(new.pop())
print(new.pop())


set1 = {12,13,14,15,16,3,5}
set2 = {17,18,19,20,3,5}
print(set1.union(set2))
print(set1.intersection(set2))