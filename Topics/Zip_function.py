""" The zip function returns a zip object, 
which is an iterator of tuples where the first item in each passed iterator is paired together,
and second passed iterator are paired together. 
"""

L1 = [5, 6, 7, 8]
L2 = [2, 3, 4, 9]
L3 = [20, 30, 40, 90]

print(list(zip(L1, L2)))
print(list(zip(L1, L2,L3)))

for i in zip(L1, L3):
    print(i)

print([i-j for i,j in zip(L1, L2) ])
print([j+i for j,i in zip(L1, L2) ])
print([j*i for j,i in zip(L1, L2) ])
print([j*i for j,i in zip(L1, L3) ])

Student_name = ["aryan", "snehal", "goli","icey"]
Roll_number = [1,2,3,4]
print(list(zip(Student_name,Roll_number)))