# # Print from 1 to 5
# i=1
# while i <=5:
#     print("The number is",i)
#     i+=1
# print("loop ended")


# Print from 5 to 1
i=5
while i >=1:
    print("The number is",i)
    i-=1
print("loop ended")


# Print the series by square of numbers(1,4,9,16,25,36,49,64,81,100)
n=1
while n <=10:
    print("the square is of ",n,"is: ")
    print(n**2)
    n+=1

# Print the series(1,4,9,16,25,36,49,64,81,100)    

num = [1,4,9,16,25,36,49,64,81,100]
index = 0
while index < len(num):
    print(num[index])
    index+=1