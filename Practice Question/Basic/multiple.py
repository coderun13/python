# check if number is a multiple of 7 or not
#Logic = take input then check by if num%== 0 then print

num =int(input("Enter a number: "))

if(num%7 == 0):
    print("It is a multiple of 7")
elif(num%7 != 0):
    print("It is not a multiple of 7")