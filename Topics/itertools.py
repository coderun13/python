# itertools: product, permutations, combination, accumulation, groupby and infinite iterators
# Product: it will combine the numbers or text
# Permutation: return all possible orderings of an input
# Combination: make all possible combination with specified length
# Accumulate: makes an iterator to return accumulated sums
# Groupby: returnns keys and groups 
# infinite iterator: cycle, count, repeat


from itertools import cycle, repeat, count

a = [1,2,3]
for i in repeat(1,4):
    print(i)

# a = [1,2,3]
# for i in cycle(a):
#     print(i)

# for i in count(10):
#     print(i)
#     if i == 15:
#         break


# from itertools import groupby
# def smaller_than_3(x):
#     return x<3

# a = [1,2,3,4]
# group_obj = groupby(a, key = smaller_than_3)

# for key, value in group_obj: 
#     print(key, list(value))


# from itertools import accumulate
# import operator
# a = [1,2,3,4]
# acc = accumulate(a, func=operator.mul)
# acc = accumulate(a)
# print(a)
# print(list(acc))


# from itertools import combinations, combinations_with_replacement
# a = [1,2,3,4]
# comb = combinations(a,2) #(a , length)
# print(list(comb))
# comb_wr = combinations_with_replacement(a,2)
# print(list(comb_wr))


# from itertools import permutations
# a = [1,2,4]
# perm = permutations(a)
# print(list(perm))
# perm = permutations(a,2)
# print(list(perm))


# from itertools import product
# a = [1,2]
# b = [3,4]
# pro = product(a,b)
# print(list(pro))