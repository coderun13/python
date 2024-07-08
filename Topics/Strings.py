#String is a datatype that stores a sequence of character.
# length of str = len(str)
# Escape sequence characters are special characters used for formatting.(\n)

str1 = "Basics of"
print(len(str1)) #str length
print(str1[1]) #indexing

str2 = " python"
print(len(str2))

print(str1+str2) #concatenation
print(len(str1+str2))

#Slicing = Accessing parts of a string [starting index: ending index)

str = "Snehal"
print(str[1:5]) #5 is not induced #neha
print(str[-5:-1]) #neha

# String Function
# str.endswith() returns true or false
# str.capitalize
# str.replace(old,new)
# str.find(word) returns 1st index of 1st occurrer
# str.count()

#take user name as input and print its length

name= input("What's your name: ")
print(len(name))

#find the occurence of $ in a string

str2 = "I am $ symbol here"
print(str2.find("$"))
print(str2.count("$"))
