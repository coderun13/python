#if-elf-else statement
# if statement always check the condition but elif statement checks when if statement is false.

light = "green"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("wait")
else:
    print("light is broken")

# Grade student on the basis of marks 

marks = int(input("Inter your marks: "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks <80):
    grade = "C"
else:
    grade = "D"
print("Grade of the student is-> ", grade)

# Check if a number by user is odd or even

num =int(input("Enter a number: "))

if(num%2 == 0):
    print("Number is even")
elif(num%2 != 0):
    print("Number is odd")

# Check greatest of 3 numbers entered by the user

num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))
num3 = int(input("Enter Third number: "))

if(num1 > num2 and num1 > num3):
    print("First number is greatest")
elif(num2 > num1 and num2 > num3):
    print("Second number is greatest")
else:
    print("Third number is the greatest")

# check if number is a multiple of 7 or not

num =int(input("Enter a number: "))

if(num%7 == 0):
    print("It is a multiple of 7")
elif(num%7 != 0):
    print("It is not a multiple of 7")

    