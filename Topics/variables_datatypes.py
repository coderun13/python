#Variable= It is a name given to a memory location in a program.

name = "Snehal" 
age = 19

print(name)
print(age)

print("My name is", name)
print("My age is",age)

age2 = age
print(age2)

print(type(name))
print(type(age))

#Data types
# Integer
# String
# Float
# Boolean (True, False)
# None

old = False
a = None

print(type(old))
print(type(a))

# Keywords are reserved words in python
# These can't be used as identifier.

# Print Sum
a=300
b=400
sum= a+b
print(sum)
print(type(sum))

#comment
"""multi
line comment"""

#input() statement is used to accept values from user
#input() result for it is always a str
#int(input()) this is int

name = input("Enter your name: ")
print("Welcome",name)

int("19")
val =int(input("enter some value:"))
print(type(val),val)
