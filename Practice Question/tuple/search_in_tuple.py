# Search number in tuple
#take the input, start i with 0 then i less than length of tuple then if i = index then print

tup = (1,4,9,16,25,36,49,64,81,100)
n = int(input("Enter a number: "))
i = 0
while i < len(tup):
    if(tup[i] == n):
        print("Found at index:",i)
    i+=1