# When a function calls itself repeatedly.
#call stack

# print n to 1 backwards
def show(n):
    if(n == 0): #base case = where recursion stops
        return
    print(n)
    show(n-1)

show(5)