# Collections module implement special container datatypes and alternatives functionality as 
# compared to the general built in containers like dictionaries and list etc.
# Five different types of collections: Counters, nametuple, orderedDict, defaultdict, deque
# Counter: Conatiner that stores elements in dictionary keys and counts as thier dictionary values
# Nametuple: easy and light weight to create object type similar to a structure 
# OrderDict: Like regular dict but they remember the order of the item inserted.
# Defaultdict: It will have a default key for the value not inserted yet 
# Deque: doubled ended queue

from collections import deque
d = deque()
d.append(1)
d.append(2)
d.append(3)
print(d)

d.appendleft(4)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.extend([5,6,7])
print(d)

d.rotate()
print(d)

d.rotate(2)
print(d)

# from collections import defaultdict
# d = defaultdict(int)
# d ['a'] = 1
# d ['b'] = 2
# d ['c'] = 3
# d ['d'] = 4
# d ['e'] = 5
# d ['f'] = 6
# print(d['g'])


# from collections import OrderedDict
# order_dict = OrderedDict()
# order_dict['a'] = 1  
# order_dict['b'] = 2  
# order_dict['c'] = 3  
# order_dict['d'] = 4  
# order_dict['e'] = 5  
# print(order_dict)


# from collections import namedtuple
# Num = namedtuple('Num','x,y')
# pt = Num(2,3)
# print(pt)


# from collections import Counter
# c = ('aaabbbbccccc')
# my_counter = Counter(c)
# print(my_counter)
# print(my_counter.most_common(1))
# print(my_counter.elements())
# print(list(my_counter.elements()))