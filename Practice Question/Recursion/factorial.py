# by function call
# take an input, take fact as 1 then factorial is fact*1 where range is (1, n+1)

n = int(input("Enter a number: "))

# def fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact*=i
#     print("factorial of",i,":",fact)

# fact(n)

# by recursion
# n should not be 0 or 1 then fact is n*fact(n-1)

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
    

fact(n)
print("The factorial of",n, "is:",fact(n))   