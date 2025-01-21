# logic = 0, 1, 1, 2, 3, 5, 8, 13, ....
# a = 0 , b = 1 , c = (a+b), then a = b, b = c, c = a+b
# take m as input then if m  1 then print a else print a and b for c range 
# is (2 to m+1) c= a+b, a = b, b = c then print c 
a = 0
b = 1

m = int(input("Enter the number for series: "))
if m ==1:
    print(a)
else:
    print(a)
    print(b)
for i in range(2, m):
    c = a+b
    a = b
    b = c
    print(c)