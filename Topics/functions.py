# Function->Block of code that perform a specific task.
# Built-in Functions -> print(), len(), type(), range()
# User-Defined Functions 
# Default parameters -> Assigning a default value to parameter,which is used when no argument is passed.

def sum(a,b): #parameters
    s = a+b
    return s
print("the sum is:",sum(2,3)) #function call; arguments

# average of three numbers
def cal_avg(a,b,c):
    sum = a + b + c
    avg = sum /  3
    print(avg)
    return avg
print("The avg is:",cal_avg(1,2,3))

print("snehal", end=" ") #sep = " "
print("singh") #end = "\n"