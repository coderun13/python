# by function call
n = int(input("Enter a number: "))

# def fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact*=i
#     print("factorial of",i,":",fact)

# fact(n)

#by recursion
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
    

fact(n)
print("The factorial of",n, "is:",fact(n))   