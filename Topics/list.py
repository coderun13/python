# A built-in data type that stores set of values
# It can store elements of different types(int,float,string)
# string -> immutable(can access but can't change)
# lists -> mutable (can change)

marks = [45,34,56,78,91]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[1])

student = ["aryan", 91, 13, "bokaro"]
print(student)

#list slicing
# list_name[starting_idx: ending_idx](ending idx is not included)

print(marks[0:3])
print(marks[1:])
print(marks[-3:-1])

# List Methods
# list.append() -> adds one element at the end
# list.sort() -> sorts in ascending order 
# list.sort(reverse=True) -> sorts in descending order 
# list.reverse() -> reverse list 
# list.insert(idx,el) -> insert element at index
# list.remove -> removes first occurence of element
# list.pop(idx) ->removes element at idx

list = [2,1,3]
list.append(4)
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.reverse()
print(list)

list.insert(1, 5)
print(list)

list.remove(5)
print(list)

list.pop(2)
print(list)