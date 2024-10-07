# They are used to store data values in key:value pairs
# They are unordered, mutable(changeable) and don't allow duplicate keys, overwrite 

info = {
    "name": "snehal",
    "cgpa": 8.1,
    "marks": [98,97,95],
    "subjects": ("c","java","python"),
}

print(info)
print(type(info))
print(info["name"])
info["surname"] = "singh"
print(info)


null_dict = {} #null dictionary
null_dict["name"]= "Icey"
print(null_dict)


# Nested Dictionary
student={
    "name": "aryan",
    "marks": {
        "maths":"98",
        "english": "99",
    },
    "age":"14"
}
print(student)
print(student["marks"])
print(student["marks"]["english"])


# Dictionary methods

# myDict.keys() -> returns all keys
# myDict.values() -> returns all values
# myDict.items() -> returns all (key val) pairs as tuple
# myDict.get("key"") -> returns the key according to value
# myDict.Update({newDict}) -> Insert the specified items to the dictionary


print(student.keys())
print(list(student.keys())) #typecasting in list

print(len(student.keys()))
print(student.values())

print(student.items())
pairs = list(student.items())
print(pairs[1])

print(student.get("name"))
student.update({"name":"rahul"})
print(student.get("name"))