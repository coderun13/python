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
student1 = student[2]
print(student1)

#multiple list
mylist = [0] * 5
print(mylist)

mylist2 = [1,2,3,4,5]
new_list = mylist + mylist2
print(new_list)

list_cp = mylist
print(list_cp)

#list slicing
# list_name[starting_idx: ending_idx](ending idx is not included)

print(marks[0:3])
print(marks[1:])
print(marks[-3:-1])
print(marks[::2])

# List Methods
# list.append() -> adds one element at the end
# list.sort() -> sorts in ascending order 
# list.sort(reverse=True) -> sorts in descending order 
# list.reverse() -> reverse list 
# list.insert(idx,el) -> insert element at index
# list.remove -> removes first occurence of element
# list.pop(idx) ->removes element at idx
# List.copy() -> returns a copy of the list but changes in the copy will not affect the original list.

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

list_cp = list.copy()
print(list_cp)

# loop in list
for x in student:
    if "aryan" in student:
        print("yes")
        break
    else:
        print("no")

#list comprehension

mylist = [1,2,3,4,5]
b = [i*2 for i in mylist]

print(mylist)
print(b)