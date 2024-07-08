"""
Types of Operators
An operator is a symbol that performs a certain operation between operands.
Arithematic Operators(+,-,*,/,%,**)
Relational / Comparison Operators(==,!=,>,<,>=,<=)
Assignment Operators(=,+=,-=,*=,/=,%=,**=)
Logical Operators(not, and, or)
"""
#Arithmetic operators
a = 30
b = 6
sum = a + b
print(sum)
print(a-b)
print(a*b)
print(a/b) #quotient
print(a%b) #remainder
print(a**b) #a^b

#Relational operators
a = 20
b = 21
print(a == b) #False
print(a != b) #True
print(a >= b) #False
print(a > b) #False
print(a <= b) #True
print(a < b) #True

#Assignment Operators
num = 10
num = num + 10
print("num :",num)
num *= 5
print("num :", num)

#logical operators
a = 50
b = 30
print(not False)
print(not (a > b))

val1 = True
val2 = False
print("AND operator:", val1 and val2)

print("OR operator:", val1 or val2)

#Type Conversion
#conversion = automatically

a = 2 #int is converted to float
b = 4.25
sum= a+b
print(sum)

#Type Casting
#casting = manually

a = float("2") #string converted to float
b = 4.25
print(type(a))
print(a+b)

