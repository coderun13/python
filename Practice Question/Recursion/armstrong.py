# Armstrong number is the number of n digits which are equal to the sum of nth power of its digit.(example: 5 , n = 1 then power of 5 ^ 1 = 5)
# Logic:  example: 153 see here we have to find the length of the string then count the digits then add the power in result then print

for i in range(1001):
    num = i
    result = 0
    n = len(str(i))
while(i!=0):
    digit = i % 10
    result = result + digit**n
    i = i//10
if num == result:
    print("The armstrong numbers from 1 to 1000 are:",num)

