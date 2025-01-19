# Lambda dunction is a small one liner function that is defined without a name 
# used when you have to use the function once in your code or when you use higher order function
# sorted, map, reduce 
# map = (func, seq)

# reduce
from functools import reduce
a = [1,2,3,4,5,6]
product_b = reduce(lambda x,y: x*y,a)
print(product_b)

# filter
a = [1,2,3,4,5,6]
b = filter(lambda x: x%2==0,a)
print(list(b))

# map
a = [1,2,3,4,5]
b = map(lambda x: x*2,a)
print(list(b))

# sorted
points2D = [(1,2),(23,24),(12,13),(2,-1),(4,5)]
points2D_sorted = sorted(points2D, key = lambda x: x[1])
points2D_sorted = sorted(points2D, key = lambda x: x[0] + x[1])
print(points2D)
print(points2D_sorted)

add10 = lambda x: x + 10
print(add10(5))

# Same as lambda function
# def add10_func(x):
#     return x + 10

mult =  lambda x,y : x*y
print(mult(2,7))