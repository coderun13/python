# Search number in tuple
tup = (1,4,9,16,25,36,49,64,81,100)
n = int(input("Enter a number: "))
i = 0
while i < len(tup):
    if(tup[i] == n):
        print("Found at index:",i)
    i+=1