# Loops are used to repeat instructions
# While loop
# For loop
# Break: Used to terminate the loop when conected
# Continue: Terminates execution in the current iteration and continues execution of the loop with next iteration
# range(): It returns a sequence of numbers, starting from 0 by default, and increments by 1, and stops before a specified number. 

count = 1
while count <=5:
    print("hello snehal",count)
    count +=1
print(count)


# i=1
# while i<=5:
#     print(i)
#     if(i==3):
#         break
#     i+=1


n=0
while n<=5:
    if(n==3):
        n+=1    
        continue
    print(n)
    n+=1


nums = [11,22,33,44,55]
for val in nums:
    print(val)


tup = (6,7,8,9,10)
for val in tup:
    if(val == 9):
        print("9 found") 
        break 
    print(val)
else:
    print("end")  

# range(start,stop,step)
for el in range(1,6,2):
    print(el)