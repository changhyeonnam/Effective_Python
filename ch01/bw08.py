names = ['Cecilia','남궁민수','jimmy']
counts =[len(n) for n in names]
print(counts)
# [7, 4, 5]


# for i in range(len(names)):
#     count = counts[i]
#     if count>max_count:
#         longest_name = names[i]
#         max_count = count
# print(longest_name)
#
# longest_name = None
# max_count = 0
# for i,name in enumerate(names):
#     count = counts[i]
#     if count > max_count:
#         longest_name=name
#         max_count = count
#
# for name,count in zip(names,counts):
#     if count > max_count :
#         longest_name = name
#         max_count = count
#
names.append('Rosalind')
# for name,count in zip(names,counts):
#     print(name)

import itertools
for name,count in itertools.zip_longest(names,counts):
    print(f'{name} : {count}')
# Cecilia : 7
# 남궁민수 : 4
# jimmy : 5
# Rosalind : None
def zipx(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)

test_tuple = zipx(names,counts)
print(next(test_tuple))
# print(next(test_tuple))
# print(next(test_tuple))
# print(next(test_tuple,-1))
#
# listx = [1,2,4,5,6,7]
# print(tuple(listx))
import collections,types
print(isinstance(test_tuple,types.GeneratorType))